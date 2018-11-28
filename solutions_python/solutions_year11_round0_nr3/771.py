#!/usr/bin/python

N = 30  #the number of bits for an integer, log(10**6*1000,2)
#N = 24  #the number of bits for an integer, log(10**6*15,2)

def int2b(n, bit=N):
    return [(n >> i) & 1 for i in range(bit)[::-1]]

def kidadd(l1, l2, bit=N):
    result = [0]*N
    for i in range(N)[::-1]:
        result[i] = l1[i] ^ l2[i]
    return result

def b2int(l, bit=N):
    result = 0
    for i in range(bit):
        if l[i]:
            result += (l[i]<<(N-i-1))
    return result

def kidsum(l):
    return b2int(reduce(kidadd, map(int2b, l)))

if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        f.readline()
        C = map(int,f.readline().strip().split())
        if kidsum(C):
            res = 'NO'
        else:
            res = str(sum(C) - min(C))
        print 'Case #%d: %s'%(i+1,res)

    
