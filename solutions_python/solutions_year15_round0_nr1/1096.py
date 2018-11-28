import sys

inf = open('First-large.in','r')

T = [int(x) for x in inf.readline().split()][0]

for t_case in range(1,T+1):
    max_shy, shy_array = inf.readline().split()
    max_shy = int(max_shy)
    
    worst = 0
    cumulative = 0
    for idx in range(0, len(shy_array)):
        cumulative += int(shy_array[idx])
        worst = max(worst, idx+1-cumulative)
    
    print 'Case #%d: %d' % (t_case, worst)
    
