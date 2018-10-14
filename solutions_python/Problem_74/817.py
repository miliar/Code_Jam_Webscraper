fp = open("A-large.in")
def get():
    return fp.readline().strip()

class Robot:
    def __init__(self):
        self.x = 1
        self.targets = []
        self.canpush = False
    
    def step(self):
        if self.targets:
            t = self.targets[0]
            if self.x < t:
                self.x += 1
                return 0
            if self.x > t:
                self.x -=1
                return 0
            if self.canpush:
                self.targets = self.targets[1:]
                self.canpush = False
                return 1
        return 0
    
    def done(self):
        return not self.targets
    
def solve(s):
    row = s.split()
    n = int(row[0])
    commands = row[1:]
    assert(len(commands) == n*2)
    robots = {'O':Robot(), 'B':Robot()}
    order = []
    for i in xrange(n):
        r = commands[i*2]
        button = int(commands[i*2+1])
        robots[r].targets.append(button)
        order.append(r)
    ans = 0
    haspushed = 1
    while not all(r.done() for r in robots.itervalues()):
        if haspushed:
            robots[order[0]].canpush = True
            order = order[1:]
            
        haspushed = sum(r.step() for r in robots.itervalues())
        ans += 1
    
    return ans

def main():
    nc = int(get())
    for i in xrange(nc):
        ans = solve(get())
        print "Case #%d: %s" % (i+1, ans)

if __name__ == "__main__":
    main()