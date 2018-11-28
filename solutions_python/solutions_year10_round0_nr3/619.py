import sys
import hashlib

class RollerCoasterSimulator(object):
    def __init__(self, runs, seats, groups):
        self.runs = runs
        self.seats = seats
        self.groups = groups
        self.ticketPrice = 1
        self.nextInLine = 0
        self.queues = []
        self.queueHashes = []
        self.queueResetPos = 0

    def run(self):
        self.buildQueues()

        p = 0
        nq = 0
        for x in xrange(self.runs):
            p += self.queues[nq]
            nq = nq + 1 if nq != len(self.queues) - 1 else self.queueResetPos

        return p * self.ticketPrice

    def buildQueues(self):
        def hashQueue(q):
            return hashlib.sha1("-".join(map(str, q))).digest()

        def sumQueue(q):
            return sum(map(lambda x: self.groups[x], q))

        def getNextQueue():
            s = self.seats
            q = []
            c = 0

            while True:
                if self.nextInLine in q:
                    break
                ngc = self.groups[self.nextInLine]
                if c + ngc > s:
                    break
                c += ngc
                q.append(self.nextInLine)
                self.nextInLine = self.nextInLine + 1 if self.nextInLine != len(self.groups) - 1 else 0
            return q

        qc = 0

        while True:
            q = getNextQueue()
            h = hashQueue(q)

            if h in self.queueHashes:
                self.queueResetPos = self.queueHashes.index(h)
                break
            
            self.queueHashes.append(h)
            self.queues.append(sumQueue(q))

def main(fn):
    with open(fn) as f:
        cases = int(f.readline())
        for x in xrange(cases):
            z = map(int, f.readline().split())
            groups = map(int, f.readline().split())
            r = RollerCoasterSimulator(z[0], z[1], groups).run()
            print "Case #%s: %s" % (x + 1, r)

if __name__ == "__main__":
    if len(sys.argv) ==  2:
        main(sys.argv[1])
    else:
        print "Usage: %s <input_file>" % sys.argv[0]

