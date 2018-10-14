import sys
import os
import math

In = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[1])
Out = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[2],'w')

def flip(a):
    if a == '-':
        return '+'
    if a == '+':
        return '-'

if __name__ == '__main__':
    T = int(In.readline())
    for x in range(T):
        print(x+1)
        N = In.readline().rstrip('\n')
        N = list(N)
        N.reverse()
        N = ''.join(N)
        print(N)
        out = N
        k=0
        while True:
            for l in range(k+1,len(N)):
                print(out)
                if int(out[k]) >= int(out[l]):
                    print('didnt happen',k,l)
                    continue
                elif int(out[l]) > int(out[k]):
                    print('it happened',k,l)
                    out = l*'9'+str(int(N[l])-1)+N[l+1:]
                    print(out)
                    k = l-1
                    break
            k += 1
            if k == len(N):
                break
        out = list(out)
        out.reverse()
        out = ''.join(out)
        out = out.lstrip('0')

        Out.write('Case #{}: {}\n'.format(x+1,out))
