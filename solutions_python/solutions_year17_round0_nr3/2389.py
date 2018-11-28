from multiprocessing import Process, Array
import time
import sys

sys.setrecursionlimit(9999999)

class Problem(object):
    def solve(self, p, size, people, sols):
        seg = [[1, size]]
        last = None

        for i in xrange(people):
            seg_pos = 0
            seg_to_use = seg[0]
            for i, s in enumerate(seg):
                d1 = s[1]-s[0]
                d2 = seg_to_use[1]-seg_to_use[0]
                if d1 > d2 or (d1 == d2 and s[0] < seg_to_use[0]):
                    seg_to_use = s
                    seg_pos = i

            seg.pop(seg_pos)
            new_pos = (seg_to_use[1]-seg_to_use[0])/2 + seg_to_use[0]
            last = [seg_to_use[1]-new_pos, new_pos-seg_to_use[0]]
            seg.append([seg_to_use[0], new_pos-1])
            seg.append([new_pos+1, seg_to_use[1]])

        sols[2*p] = last[0]
        sols[2*p+1] = last[1]
        with open('/tmp/prob_sol', 'a') as f:
            f.write("sol (%d): %s\n" % (p, sols[p]))

probs = int(raw_input())
sols = Array('f', probs*2)

workers = []
for i in xrange(probs):
    parts = map(int, raw_input().split())
    p = Problem()
    pr = Process(target=p.solve, args=(i, parts[0], parts[1], sols))
    pr.start()
    workers.append(pr)

for w in workers:
    w.join()

count = 1
for i in xrange(probs):
    print "Case #%d: %d %d" % (i+1, sols[2*i], sols[2*i+1])
    count += 1
