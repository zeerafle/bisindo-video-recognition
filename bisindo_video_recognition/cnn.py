import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input


class CenterSquareCrop(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(CenterSquareCrop, self).__init__(**kwargs)

    def call(self, inputs):
        # Get the dynamic shape of the input image
        shape = tf.shape(inputs)
        height = shape[1]
        width = shape[2]
        # Determine the side length of the largest possible central square
        crop_size = tf.minimum(height, width)
        # Compute offsets for centering the crop
        offset_height = (height - crop_size) // 2
        offset_width = (width - crop_size) // 2
        # Crop the central square from each image in the batch
        return tf.image.crop_to_bounding_box(inputs, offset_height, offset_width, crop_size, crop_size)


def build_feature_extractor(img_size, training=False):
    feature_extractor = tf.keras.applications.InceptionV3(
        weights="imagenet",
        include_top=False,
        pooling='avg',
        input_shape=(img_size, img_size, 3),
    )
    crop = CenterSquareCrop()
    resize = tf.keras.layers.Resizing(img_size, img_size)
    preprocess_input = tf.keras.applications.inception_v3.preprocess_input
    inputs = tf.keras.Input(shape=(None, None, 3))
    if training:
        augmentation = tf.keras.Sequential(
            [
                tf.keras.layers.RandomBrightness(0.2),
                tf.keras.layers.RandomContrast(0.2)
            ],
            name="augmentation"
        )
        x = augmentation(inputs)
    else:
        x = inputs
    preprocessed = preprocess_input(resize(crop(x)))

    outputs = feature_extractor(preprocessed)
    return tf.keras.Model(inputs, outputs, name="feature_extractor")
