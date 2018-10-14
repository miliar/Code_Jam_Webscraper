from multiprocessing import Process, Array
import time

class Problem(object):
    def _get_flips(self, pc, size, minim=[], flips=0, known_pos=None):
        if not known_pos:
            minim = [float('Inf')]
            known_pos = {}

        tpl_pc = tuple(pc)
        if known_pos.get(tpl_pc, float('Inf')) <= flips:
            #print "Known All:", flips+1, pc
            return minim[0]
        known_pos[tpl_pc] = flips

        correct = True
        for i in xrange(len(pc)-size+1):
            if not all(pc[i:i+size]):
                pc_aux = pc[:]
                correct = False
                #print "Flipping:", i,i+size, flips, pc_aux
                for j in xrange(i,i+size):
                    pc_aux[j] = not pc_aux[j]
                #print "Flipped:", pc_aux
                self._get_flips(pc_aux, size, minim, flips+1, known_pos)

        if correct and flips:
            minim[0] = flips
            #print "FOUND!!!!:", pc, flips

        return minim[0]

    def solve(self, p, pc, size, sols):
        if all(pc):
            sols[p] = 0
        else:
            sols[p] = self._get_flips(pc, size)
        with open('/tmp/prob_sol', 'a') as f:
            f.write("sol (%d): %s\n" % (p, sols[p]))

probs = int(raw_input())
sols = Array('f', probs)

workers = []
for i in xrange(probs):
    parts = raw_input().split()
    parts[0] = map(lambda x: x =='+', parts[0])
    p = Problem()
    pr = Process(target=p.solve, args=(i, parts[0], int(parts[1]), sols))
    pr.start()
    workers.append(pr)

for w in workers:
    w.join()

count = 1
for s in sols:
    if str(s) == 'inf':
        print "Case #%d: IMPOSSIBLE" % (count)
    else:
        print "Case #%d: %d" % (count, int(s))
    count += 1
