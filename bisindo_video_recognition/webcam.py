import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np

from bisindo_video_recognition.cnn import build_feature_extractor

IMG_SIZE = 299
MAX_SEQ_LEN = 100
label_dict = {0: 'apa kabar', 1: 'ayo jalan-jalan', 2: 'jaga kesehatan', 3: 'kamu mau kemana', 4: 'kamu tinggal dimana', 5: 'mau pesan apa', 6: 'nama kamu siapa', 7: 'salam kenal', 8: 'sama-sama', 9: 'sampai jumpa lagi', 10: 'saya minta maaf', 11: 'sekarang jam berapa', 12: 'selamat malam', 13: 'selamat pagi', 14: 'selamat siang', 15: 'terima kasih'}

print("Loading model...")
feature_extractor = build_feature_extractor(IMG_SIZE)
seq_model = load_model('models/seq_model.keras')

print("Starting webcam...")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

raw_frames = []
frame_counter = 0

print("Starting video capture. Press 'q' to quit.")

# Phase 1: Record video
while frame_counter < MAX_SEQ_LEN:
    # capture frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture frame.")
        break

    # save raw frame
    raw_frames.append(frame.copy())

    # display frame count
    frame_counter += 1
    cv2.putText(frame, f"Recording: {frame_counter}/{MAX_SEQ_LEN}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # display frame
    cv2.imshow('BISINDO Recogniniton - Recording', frame)

    # check for 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release video capture
cap.release()
cv2.destroyAllWindows()
print ("Video capture completed. Processing frames...")

# Phase 2: Process frames
print("Extracting features...")
features_sequence = feature_extractor.predict(np.array(raw_frames), batch_size=100)
print("features_sequence shape:", features_sequence.shape)
# add batch dimension
features_sequence = np.expand_dims(features_sequence, axis=0)

# Phase 3: Making prediction
print("Making prediction")
mask = np.ones((1, MAX_SEQ_LEN), dtype="bool")
prediction = seq_model.predict({'features': features_sequence, 'mask': mask})
print('prediction result:', prediction)

predicted_class = np.argmax(prediction[0])
confidence = prediction[0][predicted_class] * 100

print(f"Prediction: {label_dict[predicted_class]} with {confidence:.2f}% confidence")
