import math

global tree

def addPath(path, flag):
  global tree
  parts = path.split("/")
  p = tree
  for part in parts[1:]:
    if part not in p: p[part] = [{}, flag]
    p = p[part][0]

def countDirs(tree):
  count = 0
  for p in tree:
    count += countDirs(tree[p][0])
    if not tree[p][1]: count += 1
  return count 

lines = open("input.txt").readlines()
cases = int(lines[0])
line_num = 1
for case in xrange(1, cases + 1):
    global tree 
    tree = {}
    n,m = (int(t) for t in lines[line_num].split())
    for i in xrange(n):
      line_num += 1
      addPath(lines[line_num].strip("\n"), True)
    for i in xrange(m):
      line_num += 1
      addPath(lines[line_num].strip("\n"), False)
    line_num += 1
    #print tree
    print "Case #%d: %d" % (case, countDirs(tree))
    
