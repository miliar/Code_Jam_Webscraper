'''
Created on May 22, 2011

@author: jagadeeshe
'''
import math

def create_data_stream():
    from sys import stdin
    file_content = stdin.read()
    segs = file_content.split()
    segs.reverse()
    
    def read():
        return segs.pop()
    
    def readInt():
        return int(segs.pop())
        
    class _A(object): pass
    
    obj = _A()
    obj.read = read
    obj.readInt = readInt
    return obj


def codejam(solution):
    data_stream = create_data_stream()
    T = data_stream.readInt()
    for case in range(T):
        result = solution(data_stream)
        print "Case #%s: %s" % (case+1, result)


def divides(a, b):
    if a < b:
        return b % a == 0
    else:
        return a % b == 0

def harmony(data_stream):
    N = data_stream.readInt()
    L = data_stream.readInt()
    H = data_stream.readInt()
    others = [data_stream.readInt() for _ in range(N)]
    
    while L <= H:
        found = True
        for d in others:
            if not divides(d, L):
                found = False 
                break
        if found:
            return L
        L += 1
    return 'NO'

if __name__ == '__main__':
    codejam(harmony)
