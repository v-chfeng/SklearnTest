#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'k neighbor'

import numpy as np
import scipy

from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
iris = load_iris()
print(iris.data.shape)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22, test_size=0.25)

from sklearn.preprocessing import 