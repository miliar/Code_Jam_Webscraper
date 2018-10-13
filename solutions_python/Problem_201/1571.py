import numpy as np
from numba import jit

# Input
#file = "C-small-1-attempt1.in"
file = "C-small-2-attempt0.in"
text = [line.rstrip() for line in open(file, 'r')]
cases = text[0]
values = text[1:]

# Functions
def getcenter(N):
    if N%2 == 0:
        return np.floor(N/2)
    else:
        return np.ceil(N/2)

            
# Run cases
result = []
for case in values:
    N,K = case.split(" ")
    N = int(N)
    K = int(K)
    while K >= 2:
        c = getcenter(N)
        K -= 1
        if K%2 == 0:
            N = c-1
        else:
            N = N-c
        K = np.ceil(K/2)
    c = getcenter(N)
    result.append([int(max(c-1, N-c)), int(min(c-1, N-c))])

# Output
file = open("output.txt", 'w')
for i in range(len(result)):
    file.write("Case #{:d}: {:d} {:d}\n".format(i+1, result[i][0], result[i][1]))
