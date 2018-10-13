import sys
from collections import deque

if len(sys.argv) != 3:
    print("Usage: python scriptD.py <input_file> <output_file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

def play_war(naomi, ken):
    n = deque(sorted(naomi))
    k = deque(sorted(ken))
    while len(k) > 0 and len(n) > 0:
        if n[0] < k[0]: n.popleft()
        k.popleft()
    return len(n)

def play_deceitful_war(naomi, ken):
    n = deque(sorted(naomi))
    k = deque(sorted(ken))
    p = 0
    while len(n) > 0:
        if n[0] > k[0]:
            n.popleft()
            k.popleft()
            p += 1
        else:
            n.popleft()
            k.pop()
    return p

results = []
with open(input_file, 'r') as f:
    T = int(f.readline())
    for t in xrange(T):
        N = int(f.readline())
        naomi = map(float, f.readline().split())
        ken = map(float, f.readline().split())
        y = play_deceitful_war(naomi, ken)
        z = play_war(naomi, ken)
        results.append('Case #%d: %d %d\n' % (t+1, y, z))

with open(output_file, 'w') as f:
    f.writelines(results)