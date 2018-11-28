'''
Created on 14-Apr-2012

@author: dushyant
'''

import sys

def findComb(t,p):
    result = []
    solution = False
    surprise = True
    for i in range(p,11):
        for j in range(i-2,i+1):
            for k in range(i-2,j+1):
                if (i + j + k) == t and j >= 0 and k >= 0:
                    solution = True
                    if (i - k <2 ):
                        surprise = False
                        
                    result.append((i, j, k))
#    print result, surprise
    return solution, surprise

def solve(N, S, p, ts):
    count = 0
    sur_count = 0
    for t in ts:
        sol, sur = findComb(int(t),p)
        if not sol:
            continue
        
        if sur:
            sur_count += 1;
        else:
            count += 1
    return count + min(S, sur_count)
    
def main():
#    print findComb(8,4)
    ofp = open(sys.argv[2],'w')
    with open(sys.argv[1],'r') as ifp:
        T = int(ifp.readline())
        for i in range(T):
            words = ifp.readline().strip().split()
            N = int(words[0])
            S = int(words[1])
            p = int(words[2])
            ofp.write("Case #%d: %d\n"%(i+1, solve(N, S, p, words[3:])))
    
    ofp.close()
if __name__ == '__main__':
    main()