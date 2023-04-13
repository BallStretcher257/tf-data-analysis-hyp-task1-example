import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 625760313  # Ваш chat ID, не меняйте название переменной


def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success)/(x_cnt + y_cnt)
    z = (p1 - p2)/(np.sqrt(p*(1-p)*(1/x_cnt + 1/y_cnt)))
    return z >= norm.ppf(1-0.06) # Ваш ответ, True или False
