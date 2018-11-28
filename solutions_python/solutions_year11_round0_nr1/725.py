import psyco
psyco.full()
import sys


class Step(object):
    def __init__(self, req, ob, button):
        self.req = req # required Step
        self.ob = ob # 'O' or 'B'
        self.button = button # button number

def calc(seq):
    p = {'O':1, 'B':1}
    oseq = [step for step in seq if step.ob=='O']
    bseq = [step for step in seq if step.ob=='B']
    dones = set()
    def iter(seq):
        if len(seq) == 0:
            return None
        s = seq[0]
        req = s.req
        if (req == None or req in dones) and p[s.ob]==s.button:
            return seq.pop(0) # push button
        else:
            diff = s.button-p[s.ob]
            if diff != 0:
                p[s.ob] += diff/abs(diff) # move one toward
            else:
                pass # wait
            return None # not done yet
    t = 0
    for step in seq:
        while not step in dones:
            addDones = [] 
            addDones.append(iter(oseq))
            addDones.append(iter(bseq))
            for ad in addDones:
                if ad != None:
                    dones.add(ad) # push button
            t += 1
    return t

def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    seq = []
    ob=None
    for i,t in enumerate([s for s in line.split(' ')][1:]):
        if i%2==0:
            ob = t
        else:
            if len(seq) > 0:
                prevStep = seq[-1]
            else:
                prevStep = None
            button = int(t)
            seq.append(Step(prevStep, ob, button))
    v = calc(seq)
    print "Case #%d: %s" % (cn,str(v))
    cn += 1
