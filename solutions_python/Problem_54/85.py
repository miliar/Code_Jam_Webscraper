import sys
from functools import reduce

fin = open('in.txt','r')
fout = open("out.txt","w")
sys.stdout = fout

def gcd(a,b):
    while (a != 0): a,b = b%a,a
    return b

ncas = int(fin.readline())
for cas in range(ncas):
    line = fin.readline().split()
    n = int(line[0])
    g = [int(x) for x in line[1:]]
    
    dif = []
    for i in range(n-1):
        dif.append(abs(g[i+1] - g[i]))    
    r = reduce(gcd,dif)
    res = g[0] % r
    if (res != 0): res = r - res
    print ("Case #{}: {}".format(cas+1,res));