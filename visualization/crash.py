from keras.layers import Input, Dense
from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Activation
import keras.callbacks as C
import numpy as np
from math import log10
import tensorflow as tf
import keras.backend as K



class LossHistory(C.Callback):

    def on_train_begin(self, logs={}):
        #initialization of the empty dataset
        self.losses = []


    def on_train_end(self, logs={}):
        # saving dataset into csv

        print(model.layer)

        losses_to_save = np.array(self.losses, dtype='float32')
        np.savetxt('loss.csv', losses_to_save, header="x,y", comments="", delimiter=",")


    def on_batch_end(self, batch, logs={}):
        # at each batch we compute historic
        self.losses.append([len(self.losses), logs.get('loss')])

    def mean_magnitude(self, weights, bias):
        mean_magnitude = np.append(weights, bias)
        n = float(mean_magnitude.size)
        mean_magnitude = np.square(mean_magnitude)
        mean_magnitude = np.sum(mean_magnitude)
        mean_magnitude = np.divide(mean_magnitude, n)
        mean_magnitude = np.sqrt(mean_magnitude)
        # mean_magnitude = np.log10(mean_magnitude)
        print(mean_magnitude)
        return mean_magnitude



x_train = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")


# the four expected results in the same order
y_train = np.array([0, 1, 1, 0], "float32")

model = Sequential()
# additionner les dimensions
model.add(Dense(200, input_dim=2, activation='relu'))
model.add(Dense(300, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])



model.fit(x_train, y_train, batch_size=10, epochs=10, verbose=2, callbacks=[LossHistory()])
