import random
import numpy as np

class Network:
    def __init__(self, sizes):
        self.num_layer = len(sizes)
        self.sizes = sizes #represents number of neurons in each layer
        self.biases = [np.random.randn(y,1) for y in sizes[1:]] #initialise the biases randomly with Gaussian distribution of mean 0 and standard deviation 1
        self.weights = [np.random.randn(y,x) 
                for x,y in zip(sizes[:-1], sizes[1:])] #ditto as above
#The code assumes that the first layer is an input layer, and so it 
# doesnt assign any weights or biases to it
    
    def feedforward(self, a):
        #Return the output of the network is "a" is input
        for b,w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w,a)+b)
        return a
    

def sigmoid(z):
    sig = 1.0/(1.0+np.exp(-z))
    return sig
    