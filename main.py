import numpy as np
import random as rand
import math

LAYER_SIZE = 3
INPUT_SIZE = 4

def sigmoid(x):
    return 1/(1+math.exp(-x))
def forwardLayer(weightArray, thisLayer, nextLayer):
    rows = weightArray.shape[0]
    columns = weightArray.shape[1]
    for y in range(0, columns):
        temp = 0
        print(y)
        for x in range(0, rows):
            temp = temp + input[x] * weightArray[x][y]
        nextLayer[y][0] = sigmoid(temp)
    return nextLayer
def forwardFinishLayer(weightArray, thisLayer):
    rows = weightArray.shape[0]
    columns = weightArray.shape[1]
    temp = 0
    for y in range(0, rows):
        temp = temp + weightArray[y][0]
    return sigmoid(temp)
def initWeights(weightArray):
    for x in range(0, weightArray.shape[0]):
        for y in range(0, weightArray.shape[1]):
            weightArray[x][y] = rand.random()
    return weightArray


input = np.arange(INPUT_SIZE).reshape(INPUT_SIZE, 1)
input[0] = 2
input[1] = 9

hidden = np.arange(LAYER_SIZE, dtype = "f").reshape(LAYER_SIZE, 1)
output = np.arange(1)

print("Input Layer: \n", input)
print("Hidden Layer 1: \n", hidden)

inputWeights = np.ones((INPUT_SIZE,LAYER_SIZE), dtype="f")

inputWeights = initWeights(inputWeights)

print("Input Weights: \n", inputWeights)

outputWeights = np.ones((LAYER_SIZE, 1))
outputWeights = initWeights(outputWeights)

print("Output Weights: \n", outputWeights)

hidden = forwardLayer(inputWeights, input, hidden)
print("Hidden Forwarded: \n", hidden)

output = forwardFinishLayer(outputWeights, hidden)
print("Output: \n", output)