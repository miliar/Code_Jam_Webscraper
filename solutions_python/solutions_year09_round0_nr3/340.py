import sys, re
filename = sys.argv[1]
f = open(filename)
N = int(f.readline())

def find_match(p, wc):
  if len(wc) == 0:
    return 1
  elif len(wc) > p:
    return 0
    
  found = 0
  while p.find(wc[0]) != -1:
    pos = p.find(wc[0])
    found += find_match(p[pos+1:], wc[1:])
    p = p[pos+1:]

  return found

welcome = 'welcome to code jam'
for c in range(N):
  case = f.readline().strip()
  case = ''.join([ch if ch in welcome else '' for ch in case])
  print "Case #%d: %s" % (c+1, `find_match(case, welcome)`[-4:].zfill(4))