'''
cat test_b.txt | python problem_b.py
cat B-small-attempt1.in | python problem_b.py >B-small-attempt1.out
cat B-large.in | python problem_b.py >B-large.out
'''

from sys import stdin

DELTA = 0
FLOW = 1

def main():
    tt = int(stdin.readline().strip())
    for t in xrange(1, tt+1):
        (n, v, x) = (float(s) for s in stdin.readline().strip().split(' '))
        n = int(n)
        flow = 0.0
        cold = list()
        warm = list()
        for _ in xrange(n):
            (r, c) = (float(s) for s in stdin.readline().strip().split(' '))
            if c == x:
                flow += r
            elif c < x:
                cold.append([x - c, r])
            else:
                warm.append([c - x, r])
        if (len(cold) == 0 or len(warm) == 0) and flow == 0.0:
            print "Case #{}: IMPOSSIBLE".format(t)
            continue
        cold.sort()
        warm.sort()
        while len(cold) > 0 and len(warm) > 0:
            cold_capacity = cold[-1][FLOW] / warm[-1][DELTA]
            warm_capacity = warm[-1][FLOW] / cold[-1][DELTA]
            if cold_capacity < warm_capacity:
                flow_cold = cold[-1][FLOW]
                flow_warm = cold[-1][FLOW]*cold[-1][DELTA]/warm[-1][DELTA]
                #print "c<w: {} {}".format(flow_cold, flow_warm)
                flow += flow_cold + flow_warm
                cold.pop()
                warm[-1][FLOW] -= flow_warm
                if warm[-1][FLOW] < 1e-12:
                    assert warm[-1][FLOW] >= -1e-12, "{} {}".format(t, warm[-1][FLOW])
                    warm.pop()
            else:
                flow_warm = warm[-1][FLOW]
                flow_cold = warm[-1][FLOW]*warm[-1][DELTA]/cold[-1][DELTA]
                #print "c>w: {} {}".format(flow_cold, flow_warm)
                flow += flow_cold + flow_warm
                warm.pop()
                cold[-1][FLOW] -= flow_cold
                if cold[-1][FLOW] < 1e-12:
                    assert cold[-1][FLOW] >= -1e-12, "{} {}".format(t, cold[-1][FLOW])
                    cold.pop()
        print "Case #{}: {}".format(t, v/flow)
        
main()
