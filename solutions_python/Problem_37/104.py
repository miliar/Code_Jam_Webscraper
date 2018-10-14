import heapq
import sys
sys.setrecursionlimit(5000)

class Case:
    def __init__(self, s, caseNum):
        self.caseNum = caseNum
        self.bases = map(int, s.read().split(" "))

    def solve(self):
        x = 1
        while True:
            x += 1
            works = True
            for base in self.bases:
                history = {}
                converted = self.convert(x, base)
                while True:
                    total = self.total(converted)
                    if history.has_key(total):
                        works = False
                        break
                    if total == 1:
                        works = True
                        break
                    history[total] = total
                    converted = self.convert(total, base)
                if not works:
                    break
            if works:
                return x
            
    def convert(self, x, base):
        result = []
        field = base
        remainder = x
        while remainder > 0:
            amount = remainder % base
            result.insert(0,amount)
            remainder /= base
        return result
    
    def total(self, list_of_digits):
        total = 0
        for digit in list_of_digits:
            total += digit*digit
        return total
    
    def __repr__(self):
        return "Problem A Case %d" % self.caseNum

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
    
def read_header(s):
    numCases = int(s.read())
    return numCases

def run():
    import sys
    f = file(sys.argv[1])
    s = Contents(f)
    numCases = read_header(s)
    for caseNum in range(numCases):
        case = Case(s, caseNum)
        print "Case #%d: %s" % (caseNum + 1, case.solve())
        sys.stdout.flush()
        
if __name__ == "__main__":
    run()