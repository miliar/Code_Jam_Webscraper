from math import *

def printxy(l):
        l = l-2 
        if l == 0:
                print(0,0)
        elif l%2 == 0:
                print(int(l/2),int(l/2 -1))
        else:
                print(int(l//2) , (l//2))        

t = int(input())
for r in range(t):
        [N,k] = list(map(int,input().split()))
        print ("Case #",r+1,':',sep='',end = ' ')
        if k == 1 or k == 2:
                printxy(N//k+2)
        else:           
                n = int(log2(k))
                p = 2**n
                l = (N-p+1)//p
                k1 = (N-p+1)%p
                k2 = k-2**n
                if k1 > k2:
                        printxy(l+3)
                else:
                        printxy(l+2)
                        
                        
