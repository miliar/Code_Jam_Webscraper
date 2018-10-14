class Case:
    def __init__(self, s):
        self.num_flavors = int(s.read())
        self.num_cust = int(s.read())
        cust_prefs_raw = s.readList(self.num_cust)
        self.cust_prefs = []
        for line in cust_prefs_raw:
            x = line.split(" ")[1:]
            prefs = []
            for i in range(len(x) / 2):
                prefs.append((int(x[2 * i]), int(x[2 * i + 1])))
            self.cust_prefs.append(prefs)

    def solve(self):
        m = 2000000
        best = None
        for i in range(int(pow(2, self.num_flavors))):
            satisfied = False
            for cust in self.cust_prefs:
                satisfied = False
                for pref in cust:
                    if int(i & int(pow(2, pref[0] - 1)) > 0) != pref[1]:
                        continue
                    satisfied = True
                    break
                if not satisfied:
                    break
            if satisfied:
                bits = [int(i & int(pow(2, j)) > 0) for j in range(self.num_flavors)]
                m2 = sum(bits)
                if m2 < m:
                    m = m2
                    best = bits
        if best is None:    
            return "IMPOSSIBLE"
        return " ".join(map(str, best))

class Contents:
    def __init__(self, f):
        self.data = [line.strip() for line in f]
        self.i = 0

    def read(self):
        return self.readList(1)[0]

    def readList(self, len):
        result = self.data[self.i : self.i + len]
        self.i += len
        return result

import sys
f = file(sys.argv[1])
s = Contents(f)
numCases = int(s.read())

for caseNum in range(numCases):
    case = Case(s)
    print "Case #%d: %s" % (caseNum + 1, case.solve())
