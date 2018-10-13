import numpy as np

infile = open('B-large.in')
outfile = open('B-large.out', 'w')

def get_num(N):
    res = 0
    prev = 0
    strN = str(N)
    inv = False
    res = ['9']
    for i in range(len(strN)-1, -1, -1):
        if strN[i] > res[0]:
            res = [str(int(strN[i])-1)] + ['9']*len(res)
        else:
            res = [strN[i]] + res
    return int(''.join(res[:-1]))
    
T = int(infile.readline().strip())
for i in range(T):
    N = int(infile.readline().strip())
    res = "Case #{}: {}".format(i+1, get_num(N))
    #print(res)
    outfile.write(res+'\n')

infile.close()
outfile.close()
