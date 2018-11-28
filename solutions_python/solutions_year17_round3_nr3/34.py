from __future__ import division

from sys import stdin, stdout
from basics import *

EPS = 1E-9

def solve_small_1(N, K, cores, training):
    
    cores.append(1)
    cores.sort()

    for i in range(len(cores) - 1):

        diff = cores[i+1] - cores[i]
        if diff > EPS:

            if training >= (i + 1) * diff:
                training -= (i + 1) * diff

                for j in range(i+1): cores[j] += diff

            else:
                each = training / (i + 1)

                for j in range(i+1): cores[j] += each

                break

    prob = 1
    for c in cores:
        prob *= c

    return prob

T = read_val()

for t in range(T):
    N, K = read_vals()
    training = read_val(float)
    cores = read_vals(float)

    result = solve_small_1(N, K, cores, training)

    stdout.write("Case #{}: {}\n".format(t+1, result))