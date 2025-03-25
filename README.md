# BISINDO Video Recognition

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A BISINDO Indonesian sign language recognition

## How to test using webcam

0. Have Python installed
1. Clone this repo
    ```bash
    git clone https://github.com/zeerafle/bisindo-video-recognition.git
2. Install [uv](https://docs.astral.sh/uv/). Use either one of the below methods
   - `pip install uv`   (if have python installed before)
   - `curl -LsSf https://astral.sh/uv/install.sh | sh`  (for macos or linux)
   - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`   (for windows)
3. Run the following commands to set up dependencies
    ```bash
    cd bisindo-video-recognition
    uv sync
    ```
4. Download the model. The model is stored in GCP bucket as model registry. Therefore you need to have gcloud cli in your machine. Follow the instruction according to your machine in [this GCP official page](https://cloud.google.com/sdk/docs/install#installation_instructions). Alternatively, if you already have the model, put it inside `models` folder and skip step 4 and 5.
    ```bash
    # log in to gcloudcli
    gcloud auth login
    ```
5. Run the following command to pull the model (and make sure you're already have access to the bucket)
    ```bash
    uv run dvc pull models/seq_model.keras
    ```
6. Run the script
    ```bash
    uv run python -m bisindo_video_recognition.webcam
    ```


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         bisindo_video_recognition and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── bisindo_video_recognition   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes bisindo_video_recognition a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------
