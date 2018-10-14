def parse(inFile):
    n = inFile.getInt()
    vines = [inFile.getInts() for k in xrange(n)]
    dist = inFile.getInt()
    return (n, vines, dist)

class Queue:
    def __init__(self, x):
        self.q = x
        self.qat = 0
        self.qlen = len(x)
    
    def pop(self):
        self.qat += 1
        return self.q[self.qat - 1]
    
    def elements(self):
        while (not self.empty()):
            yield self.pop()

    def push(self, x):
        self.q.append(x)
        self.qlen += 1

    def empty(self):
        return self.qat == self.qlen

def solve((n, vines, dist)):
    best = [-1] * n
    best[0] = 0
    j = 1
    for i in xrange(n):
        if best[i] != -1:
            reach = vines[i][0] + min(vines[i][1], vines[i][0] - best[i])
            if reach >= dist:
                return "YES"
            while (j < n) and (vines[j][0] <= reach):
                best[j] = vines[i][0]
                j += 1
    return "NO"

if __name__ == "__main__":
    from GCJ import GCJ
    GCJ(parse, solve, "/Users/lpebody/gcj/2012_2/a/", "A").run()

            
