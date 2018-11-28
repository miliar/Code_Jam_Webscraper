'''
Created on Apr 8, 2017

@author: tortor
'''
import math
import decimal

def solve(N, K):
    
    level = math.floor(math.log2(K))+1
    
    val = (N-K)/(2**level)
    
    #print("level={} val={}".format(level,val))
    
    L = math.floor(val)
    R = int(decimal.Decimal(val).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))
    
    #print("N={} K={} L={} R={}".format(N,K,L,R))
    
    return (max(L,R), min(L,R))

def main(filename):
    with open(filename+".in") as fin:
        with open(filename+".out", "w") as fout:
            T = int(fin.readline().strip())
            
            for i in range(T):
                N, K = fin.readline().split()
                result = solve(int(N), int(K))
                #print("result=",result)
                fout.write("Case #{:d}: {} {}\n".format(i+1,result[0], result[1]))

if __name__ == '__main__':
    main("C-small-2-attempt0")