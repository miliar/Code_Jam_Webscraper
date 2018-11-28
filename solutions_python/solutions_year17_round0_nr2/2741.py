import numpy as np
from numba import njit

def to_array(inp):
    return np.array([int(a) for a in inp])

@njit
def check_tidy(x):
    dif = np.diff(x)
    if (dif >= 0).all():
        tidy = True
        i = 0
    else:
        tidy = False
        i = np.where(dif < 0)[0].min()
    return tidy, i

@njit
def adjust(x, i):
    x_a = x.copy()
    x_a[i] = x[i] - 1
    x_a[(i + 1):] = 9
    return x_a

@njit
def make_tidy(x):
    for a in range(len(x)):
        tidy, i = check_tidy(x)
        if tidy:
            return x
        else:  
            x_a = adjust(x, i)
            x = x_a.copy()
    return x

@njit
def to_int(x):
    out = 0
    for i in range(len(x)):
        out += 10**(len(x) - 1 - i) * x[i]
    return out


t = int(input()) 
for i in range(1, t + 1):
  n_str = input()
  n_ary = to_array(n_str)
  n_ary_tidy = make_tidy(n_ary)
  n_tidy = to_int(n_ary_tidy)
  # print(n_str, n_ary, n_ary_tidy, n_tidy)
  print("Case #{}: {}".format(i, n_tidy))