import sys
import os
import math

In = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[1])
Out = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[2],'w')

if __name__ == '__main__':
    T = int(In.readline())
    for x in range(T):
        print(x+1)
        N, K = In.readline().rstrip('\n').split()
        N = int(N)
        K = int(K)
        L = [N] #Components by length.
        tmp = L
        k = 0
        Max = N
        a = math.floor(math.log(N,2))
        aK = math.floor(math.log(K,2)) #We are in the aK-th row. gaps in that row are either floor(N/2**aK)-1 or floor(N/2**aK). Starts with 0-th row
        bK = K - 2**aK
        #How many floor(N/2**aK) + 1 gaps are there?
        biggaps = N - (2**aK-1)- 2**aK*(math.floor(N/2**aK)-1)
        #Are we in a floor(N/2**aK) or floor(N/2**aK)+1 gap?
        #Out.write('\n Data: N = {}, K = {}\n a = {}, aK = {}, bK = {}, biggaps = {}, math.floor(N/2**aK) = {}, lying in small gap = {}\n'.\
        #format(N,K,a,aK,bK,biggaps,math.floor(N/2**aK),bK >= biggaps))
        if bK >= biggaps:
            out_min = math.floor((math.floor(N/2**aK)-2)/2)
            out_max = math.floor((math.floor(N/2**aK)-1)/2)
        else:
            out_min = math.floor((math.floor(N/2**aK)-1)/2)
            out_max = math.floor((math.floor(N/2**aK))/2)

        Out.write('Case #{}: {} {}\n'.format(x+1,out_max,out_min))
