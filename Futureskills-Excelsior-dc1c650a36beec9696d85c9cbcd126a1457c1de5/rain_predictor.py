import pandas as pd
import numpy as np
from sklearn.externals.six import StringIO  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from numpy import array
from sklearn.model_selection import cross_val_predict

rf = RandomForestRegressor(n_estimators=1000, random_state=42)


def init():
    features = pd.read_csv('weather_data.csv')
    features = pd.get_dummies(features)
    features.iloc[:, 5:].head(5)
    labels = np.array(features['precipm'])
    features = features.drop('minpressurem', axis=1)
    features = features.drop('maxpressurem', axis=1)
    features = features.drop('meandewptm', axis=1)
    features = features.drop('maxdewptm', axis=1)
    features = features.drop('mindewptm', axis=1)
    feature_list = list(features.columns)
    print(feature_list)
    features = np.array(features)
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.30, random_state = 42)

    rf.fit(train_features, train_labels)
    # predict(test_features)


def predict(tup):
    predictions = rf.predict(tup)
    result = np.mean(predictions)
    new_res = (result / 24) * 10
    probability_of_no_rainfall = (new_res * 0.5)
    print(1 - probability_of_no_rainfall)


init()
