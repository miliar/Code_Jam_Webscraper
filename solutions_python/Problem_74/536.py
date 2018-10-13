import math

class TestCase(object):
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_input(cls, input):
        l = input.split()
        data = []
        for i in range(1, len(l), 2):
            data.append((l[i], int(l[i+1])))
        return cls(data)
    
    def solve(self):
        pos = {'O': 1, 'B': 1}
        times = {'O': 0, 'B': 0}
        curr_time = 0
        
        index = 0
        for (robot, button) in self.data:
            if pos[robot] == button:
                curr_time += 1
            else:
                curr_time += max(abs(button-pos[robot])-(curr_time-times[robot]), 0)+1
            times[robot] = curr_time
            pos[robot] = button
        return curr_time

f = open("bottrust.txt", "r")
test_cases = int(f.readline())

for i in range(test_cases):
    test_case = TestCase.from_input(f.readline())
    print "Case #%d: %d" % (i+1, test_case.solve())
