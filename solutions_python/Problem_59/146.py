import sys

def parsepath(path):
   return path.strip()[1:].split("/")

def addpath(d, path, level=0):
#   print "addpath(%s,%s,%s)" % (str(d), str(path), str(level))
   if level >= len(path):
      return 0
   ops = 0
   name = path[level]
   if name not in d:
      d[name] = {}
      ops += 1
   return ops + addpath(d[name], path, level+1)
   

f = open(sys.argv[1])
t = int(f.readline())

for ti in range(t):
   d = {}
   ops = 0
   l = f.readline().split()
   n, m = int(l[0]), int(l[1])
   for ni in range(n):
      sp = f.readline()
      p = parsepath(sp)
      addpath(d, p, 0)
   for mi in range(m):
      sp = f.readline()
      p = parsepath(sp)
      ops += addpath(d, p, 0)
   print "Case #%d: %d" % (ti+1, ops)
