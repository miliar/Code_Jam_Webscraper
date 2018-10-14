import math

lines = open("input.txt").readlines()
cases = int(lines[0])
line_num = 1

def solve(n,k,b,t,pos,speed):
  swaps = 0
  bads = 0
  in_time = []
  for i in xrange(n):
    in_time.append((b-pos[i]) <= t*speed[i])
  count = 0
  for i in xrange(n-1, -1, -1):
    if count == k: break
    if in_time[i]: 
      count += 1
      swaps += bads
    else: bads += 1
  if count == k:
    return "%d" % swaps
  else: 
    return "IMPOSSIBLE"

for case in xrange(1, cases + 1):
    (n,k,b,t) = (int(x) for x in lines[line_num].split())
    line_num += 1
    pos = [int(x) for x in lines[line_num].split()]
    line_num += 1
    speed = [int(x) for x in lines[line_num].split()]
    line_num += 1

    print "Case #%d: %s" % (case, solve(n, k, b, t, pos, speed))
    
