import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 965404933 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    alpha=0.05
    res = anderson_ksamp([x, y])
    if res.pvalue <= alpha:
        return True
    else:
        return False
