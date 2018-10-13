import sys

def getint():
  return int(sys.stdin.readline())

def getints():
  return [int(s) for s in sys.stdin.readline().split()]

def getline():
  return sys.stdin.readline().rstrip()

def solve(exist, create):
    result = 0
    fs = set()
    for c in exist:
        dirs = c.split('/')
        cur = ''
        for d in dirs[1:]:
            cur += '/' + d
            #print 'DIR:', cur
            fs.add(cur)

    for c in create:
        dirs = c.split('/')
        cur = ''
        for d in dirs[1:]:
            cur += '/' + d
            if cur not in fs:
                result += 1
                fs.add(cur)
            fs.add(cur)

    return result

T = getint()
for i in range(T):
  N, M = getints()
  exist = [getline() for j in range(N)]
  create = [getline() for j in range(M)]

  print 'Case #%d: %s' % (i+1, solve(exist, create))
#  solve(exist, create)
