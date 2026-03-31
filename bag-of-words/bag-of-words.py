import numpy as np
from collections import Counter

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    
    tokens_m = Counter(tokens)
    print(tokens_m)
    bow =[]
    
    for curr_token in range(0,len(vocab)):
        print(vocab[curr_token], end ='')
        if vocab[curr_token] not in tokens:
            bow.append(0)
        else:
            bow.append(int(tokens_m.get(vocab[curr_token], 0)))
            
    return np.array(bow, dtype=np.int64)
        
    
        
    