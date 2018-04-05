# Author: Cory Rudorf, me@coryrudorf.com

import numpy as np
import pandas as pd
import sklearn
from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.preprocessing import OneHotEncoder, StandardScaler, CategoricalEncoder
from sklearn.pipeline import Pipeline, FeatureUnion


class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


def build_pipeline(*transformers):
    """Pass a tuple of sklearn transformer objects to a sklearn Pipeline object instance. Returns pipeline object."""
    pipeline = Pipeline([
        transformers
    ])

    return pipeline


def predict_regression_model(model, dataset, labels):
    model_reg = model.fit(dataset, labels)
    model_predictions = model_reg.predict(dataset)
    return model_predictions