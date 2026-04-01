import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    
    p=np.array(p)
    y=np.array(y)

    epsilon = 1e-15
    p = np.clip(p, epsilon, 1 - epsilon)

    
    part_a = ((1-p)**gamma)* (y* np.log(p))
    part_b = (p**gamma)*(1-y)* np.log(1-p)       
    focal_loss =0
    focal_loss =  -np.mean(part_a + part_b)
    print(focal_loss)
    #   
    return focal_loss
    