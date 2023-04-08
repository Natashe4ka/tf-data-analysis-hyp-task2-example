import pandas as pd
import numpy as np
from scipy import stats

chat_id = 965404933 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat,pv = stats.ks_2samp(x, y)
    alpha=0.05
    if pv<alpha: 
        return True
    else:
        return False
