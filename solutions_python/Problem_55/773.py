import StringIO
import collections

f = StringIO.StringIO("""3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3""")

f = open('C-small-attempt0.in', 'r')

cases = int(f.readline())

for i in xrange(cases):
    answer = 0
    
    runs, hold, n = f.readline().split()
    
    hold = int(hold)
    
    groups = f.readline().split()
    
    q = collections.deque()
    for group in groups:
        q.append(int(group))
    
    max_groups = len(q)
    for j in xrange(int(runs)):
        boarded = 0
        for k in xrange(max_groups):
            if boarded + q[0] <= hold:
                boarded += q[0]
                q.rotate(-1)
            else:
                break
                
        answer += boarded
    
    print "Case #%d: %s" % (i + 1, answer)

f.close()