import sys

infile = sys.stdin

class Bot(object):
    def __init__(self, goals):
        self.pos = 1
        self.goals = goals
        
    def move(self, ticks):
        if self.goals:
            target = self.goals[0]
            if self.pos<target:
                self.pos = min(self.pos+ticks, target)
            else:
                self.pos = max(self.pos-ticks, target)
                
    def push(self):
        self.pos = self.goals[0]
        del self.goals[0]
    

def gettime(sequence):
    bseq = [s[1] for s in sequence if s[0]=='B']
    oseq = [s[1] for s in sequence if s[0]=='O']
    bots = [Bot(bseq), Bot(oseq)]
    time = 0
    for s in sequence:
        pusher, mover = (bots[0], bots[1]) if s[0]=='B' else (bots[1], bots[0])
        ticks = abs(pusher.goals[0]-pusher.pos) + 1
        pusher.push()
        mover.move(ticks)
        time += ticks
    return time
        

T = int(infile.readline())
for i in xrange(T):
    tokens = infile.readline().split()
    sequence = zip(tokens[1::2], map(int, tokens[2::2]))
    result = gettime(sequence)
    #print sequence
    print("Case #%d: %d" % (i+1, result))