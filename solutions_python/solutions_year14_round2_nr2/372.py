infile = open('in')
outfile = open('out','w')

from itertools import combinations
from copy import deepcopy
def flip(l, index):
    for i in l:
        i[index] = 1-i[index]

n = int(infile.readline())
for casecounter in range(n):
    outfile.write('Case #' + str(casecounter+1) + ': ')
    total = 0
    a,b,k = [int(i) for i in infile.readline().split()]
    print(a,b,k)
    # i'll write a smarter solution for the large case...
    for i in range(a):
        for j in range(b):
            if i&j < k:
                total += 1
    outfile.write(str(total)+'\n')
