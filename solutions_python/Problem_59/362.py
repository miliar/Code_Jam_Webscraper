
import sys
from os import path

def mkdirs(existent, create):
    fs = {}
    ret = 0
    for e in existent:
      dirs = e.split('/')
      parent = fs
      for d in dirs:
        if d == '':
            continue
        if d not in parent:
          parent[d] = {}
        parent = parent[d]

    for e in create:
      dirs = e.split('/')
      parent = fs
      for d in dirs:
        if d == '':
            continue
        if d not in parent:
          parent[d] = {}
          ret = ret + 1
        parent = parent[d]
    
    return ret



if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        line = stdin.readline()
        N, M = map(int, line.split())
        
        existent = []
        for n in range(N):
          line = stdin.readline()
          existent.append(line.strip())

        create = []
        for m in range(M):
          line = stdin.readline()
          create.append(line.strip())

        count = mkdirs(existent, create)

        print "Case #%d: %d" % (i+1, count)
