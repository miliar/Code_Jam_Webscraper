import sys
import math

def solve(diners):

    # s of sparse
    highest = max(diners)
    s = [0]*(highest+1)

    for d in diners:
        s[d] += 1

    res = highest
    best = res
    splits = 0
    while highest > 2:
        # print splits, [(i, v) for i, v in enumerate(s) if v != 0], best
        # Split the biggest pile
        half = highest/2
        half = int(math.ceil(math.sqrt(highest)))
        s[highest] -= 1
        s[half] += 1
        s[highest-half] += 1
        
        #print s
        # Find the new highest
        while s[highest] == 0 and highest > 0:
            highest -=1;
        # Update res
        splits += 1
        res = splits + highest 
#        print best, highest, splits, res
        best = min(res, best)
    return best

best = 100000

class BruteForce():

    def __init__(self, diners):
        self.highest = max(diners)
        self.s = [0]*(self.highest+1)
        self.best = self.highest
        for d in diners:
            self.s[d] += 1

    def solve(self):
        self._solve(0, self.highest)
        return self.best

    def _solve(self, minutes, highest):
        
        h  = highest
       
        while h > 0 and self.s[h] == 0:
            h -=1;
         
        best = h + minutes
        #print [(i,v) for i, v in enumerate(self.s) if v != 0], h, minutes, h+minutes, self.best 
        self.best = min(best, self.best)
        if h < 2:
            return best

        #for i in range(2, len(self.s)):

        v = self.s[h]
        if v != 0:
                for j in range(1,(h/2+1)):
                    self.s[h] -= v
                    self.s[j] += v
                    self.s[h-j] += v
                    res = self._solve(minutes+v, h)
                    best = min(res, best)
                    self.s[h] += v
                    self.s[j] -= v
                    self.s[h-j] -= v
        
        return best

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in range(T):
        D = int(sys.stdin.readline())
        v = map(int, sys.stdin.readline().split())
        #print v
        #print T, D, v
        #res = solve(v)
        #print "Case #%d: %d" % (t+1, res)
        bf = BruteForce(v)
        resb = bf.solve()
        print "Case #%d: %d" % (t+1, resb)

        #assert res == resb, str(v)

