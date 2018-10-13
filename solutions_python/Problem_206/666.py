"""
Skeleton to solve problems
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


T = int(f.readline().strip())
for c in range(T):
    D, N = map(int, f.readline().strip().split(" "))
    max_t = -1
    for i in range(N):
        ki, si = map(int, f.readline().strip().split(" "))
        max_t = max(max_t, (D - ki)/float(si))
    print("Case #%d: %s" % (c+1, D/float(max_t)))

f.close()
