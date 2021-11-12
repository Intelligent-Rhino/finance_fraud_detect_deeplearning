

### project structure:

`├── LICENSE`
`├── Rationale\ of\ the\ algorithm.pdf`
`├── data`
`│   ├── Campus+Analytics+2021+Challenge+Rules-FINAL.docx`
`│   ├── state_name.csv`
`│   ├── testset-for-participants.xlsx`
`│   └── trainset-281-29.xlsx`
`├── data_processing`
`│   └── processing.py`
`├── deepctrmodels`
`│   └── deepfm.py`
`├── model_checkpoint`
`│   ├── bst.pkl`
`│   ├── deepfm.pt`
`│   ├── max_min_scaler.pkl`
`│   ├── randomforest.pkl`
`│   ├── risk_map.pkl`
`│   └── txt_value_idx_map.pkl`
`├── notebook`
`│   ├── 00\ EDA.ipynb`
`│   ├── 02\ model-select-train.ipynb`
`│   ├── 03\ model-predict.ipynb`
`│   └── Untitled.ipynb`
`├── pipline-flow-char.pdf`
`├── requirements.txt`
`└── solution.pdf`



### explain:

1. the predict result will be saved at the root directory of the project, naming "predict_result.csv"
2. python version is Python 3.8.2, Operating System is “Mac OS”
3. run files in notebook to get exploratory, training, selection ,and also the predict result. of course, you need to install jupyter notebook firstly. You could get more detail from https://jupyter.org/ .
4. the packages used in this project are listed on file "requirements.txt"
5. downloads data from the website and put them on directory data. Specially, I download geography data from wikipedia and save them with file name "state_name.csv".
6. model and other checkpoints are all saved in directory "model_checkpoint". You don't need to create it, since you run the notebook "EDA.ipynb",the program will create it automatically.
7. reference: a. xgboost:arXiv:1603.02754v3 b. DeepFM:arXiv:1804.04950v2