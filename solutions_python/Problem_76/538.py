import math, operator, itertools

class TestCase(object):
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_input(cls, input):
        l = sorted(int(s) for s in input[1].split())
        l.reverse()
        return cls(l)
    
    def solve(self):
        values = self.data
        impossible = reduce(operator.xor, values)
        if impossible:
            return "NO"
        curr_max = 0
        for i in range(1, len(values)):
            for comb in itertools.combinations(values, i):
                sean = values[:]
                for v in comb:
                    sean.remove(v)
                if reduce(operator.xor, sean) == reduce(operator.xor, comb):
                    curr_max = max(curr_max, sum(sean))
        return curr_max

f = open("inputs/candy.txt", "r")
test_cases = int(f.readline())

for i in range(test_cases):
    test_case = TestCase.from_input((f.readline(), f.readline()))
    print "Case #%d: %s" % (i+1, test_case.solve())
