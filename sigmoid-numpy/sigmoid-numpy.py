import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x= np.array(x)
    exp_x = np.exp(-x)
    return 1/(1+exp_x)