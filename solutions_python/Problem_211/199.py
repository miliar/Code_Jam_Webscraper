#!/usr/bin/python
import math

def solve(ps,u,k):
    assert len(ps) == k
    ps.sort()
    while u > 0:
        if len(ps) > 1 and ps[0] < ps[1]:
            inc = min(u, ps[1] - ps[0])
        else:
            inc = 1
        ps[0] += inc
        u -= inc
        ps.sort()
    ans = 1.0
    for p in [(float(p)/10000) for p in ps]:
        ans = ans * p
    return ans
    


def s_to_int(s):
    s = s.strip()
    return int(s.replace('.', ''))
#    print s
 #   if s == '1.0000':
  #      return 10000
  #  else:
   #     return int(s[2:])

PATH = "/mnt/c/Users/mannes/Downloads/C-small-1-attempt1.in"
#PATH = "test.in"
f = open(PATH, "r")
lines = f.readlines()

instances = [l.strip() for l in lines[1:]]
inum = 0

while instances:
    params = instances[0].split()
    n = int(params[0])
    k = int(params[1])
    u = s_to_int(instances[1])
    ps = [s_to_int(s) for s in instances[2].split()]
    instances = instances[3:]
    print "Case #{}: {}".format(inum + 1, solve(ps,u,k))
    inum += 1
