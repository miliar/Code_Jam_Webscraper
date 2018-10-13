'''
Created on 14-Apr-2012

@author: dushyant
'''

import sys

def shift(N,s,n):
    base = pow(10,s)
    remain = N%base
    return remain * pow(10, n-s) + N/base

def solve(A, B, n):
    count = 0
    last = (-1,-1)
    for p in range(A, B+1):
        for s in range(n):
            q = shift(p, s, n)
            if p < q and q<=B and (p,q)!=last:
                count += 1
                last = (p,q)
    return count

def findDecimal(number):
    n = 0
    temp = number
    while (temp >0):
        n += 1
        temp = temp/10
    return n
 
def main():
    ofp = open(sys.argv[2],'w')
    with open(sys.argv[1],'r') as ifp:
        T = int(ifp.readline())
        for i in range(T):
            words = ifp.readline().strip().split()
            A = int(words[0])
            B = int(words[1])
            n = findDecimal(A)
            ofp.write("Case #%d: %d\n"%(i+1, solve(A, B, n)))
    
    ofp.close()

if __name__ == '__main__':
    main()