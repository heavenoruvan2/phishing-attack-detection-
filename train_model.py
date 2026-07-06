import pandas as pd,joblib
from sklearn.ensemble import RandomForestClassifier
d=pd.read_csv("dataset.csv");X=d.drop("label",axis=1);y=d.label
m=RandomForestClassifier().fit(X,y);joblib.dump(m,"phishing_model.pkl")
