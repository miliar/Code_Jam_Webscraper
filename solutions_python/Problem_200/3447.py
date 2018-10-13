from multiprocessing import Process, Array
import time
import sys

probs = int(raw_input())
sols = [0] * probs

sys.setrecursionlimit(9999999)

class Problem(object):
    def solve(self, p, n, sols):
        for i in xrange(len(n)-1, 0, -1):
            if n[i] < n[i-1]:
                if n[i-1] != 0:
                    n[i-1] -= 1

                for j in xrange(i, len(n)):
                    n[j] = 9

        sols[p] = int(''.join(map(str, n)))
        with open('/tmp/prob_sol', 'a') as f:
            f.write("sol (%d): %s\n" % (p, sols[p]))

workers = []
for i in xrange(probs):
    number = raw_input()
    p = Problem()
    p.solve(i, map(int, number), sols)

count = 1
for s in sols:
    print "Case #%d: %d" % (count, int(s))
    count += 1
