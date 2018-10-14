import math
from collections import defaultdict

class TestCase(object):
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_input(cls, input):
        num_players, lowest, highest = map(int, input[0].split())
        frequencies = map(int, input[1].split())
        return cls([lowest, highest, frequencies])
    
    def solve(self):
        lowest, highest, frequencies = self.data
        able_frequencies = None
        for freq in frequencies:
            able = self._compute_freqs(freq, lowest, highest)
            if able_frequencies is None:
                able_frequencies = able
            else:
                able_frequencies &= able
            if not able_frequencies:
                return "NO"
        return sorted(able_frequencies)[0]
        
    def _compute_freqs(self, freq, lowest, highest):
        freqs = set()
        # First compute up to sqrt
        for i in xrange(1, int(freq**0.5)+2):
            r = freq%i
            if r != 0:
                continue
            # We have a divisor
            a, b = i, freq//i
            if a > highest or b < lowest:
                break
            if lowest <= a <= highest:
                freqs.add(a)
            if lowest <= b <= highest:
                freqs.add(b)
        # Then check multiples
        if lowest <= freq <= highest:
            freqs.add(freq)
        a, b = float(lowest)/freq, float(highest)/freq
        for i in xrange(int(math.ceil(a)), int(math.ceil(b)+1)):
            r = i*freq
            if lowest <= r <= highest:
                freqs.add(r)
        return freqs

f = open("inputs/orchestra-small.in", "r")
test_cases = int(f.readline())

for i in range(test_cases):
    test_case = TestCase.from_input([f.readline().strip(), f.readline().strip()])
    print "Case #%d: %s" % (i+1, test_case.solve())
