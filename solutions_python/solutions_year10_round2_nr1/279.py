# template for Google code jam
import sys
import math
import random

def solve(N, M, E, C):
    Eset = set(E)
    total = 0
    
    tree = {}   # p: {c} 
    for path in E:
        dirs = path.split('/')
        parent = tree
        for dir in dirs:
            if not dir:
                continue
            if dir not in parent:
                parent[dir] = {}    # create
            parent = parent[dir]
    
    for path in C:
        dirs = path.split('/')
        parent = tree
        for dir in dirs:
            if not dir:
                continue
            if dir not in parent:
                parent[dir] = {}    # create
                total += 1
            parent = parent[dir]
            
    return total

def main(filename):
    f = open(filename)
    T = int(f.readline())
    for case in range(1, T+1):
        line = f.readline()
        N, M = [int(t) for t in line.split()]
        exists = []
        create = []
        for i in range(N):
            path = f.readline().strip()
            exists.append(path)
        for i in range(M):
            path = f.readline().strip()
            if path not in exists:
                create.append(path)
        res = solve(N, M, exists, create)
        print 'Case #%d:' % case,
        print '%s' % res 
        
    f.close()

if __name__ == '__main__':
    main(sys.argv[1])
    