import numpy as np
infile = open('in.txt')
outfile = open('out.txt','w')
T = int(infile.readline())

def find(n, k):
    if (k == 1):
        return ((n-1)//2, (n-1)//2+((n-1)&1))
    if (n & 1== 1):
        return find(n//2, (k-1)//2+((k-1)&1))
    else:
        if (k & 1 == 1):
            return find((n-1)//2, k//2)
        else:
            return find((n-1)//2 + 1, k//2)
        '''return find((n-1)//2+((n-1)&1), (k-1)//2+((k-1)&1))'''

for cases in range(T):
    lst = infile.readline().split()
    N = int(lst[0])
    K = int(lst[1])
    (Min,Max) = find(N,K)

    ansString = "Case #"+str(cases+1)+": "+str(Max)+' '+str(Min)+'\n'
    outfile.write(ansString)
infile.close()
outfile.close()