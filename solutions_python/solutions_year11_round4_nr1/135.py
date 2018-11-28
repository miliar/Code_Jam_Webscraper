import math

class TestCase(object):
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_input(cls, input):
        return cls(input)
    
    def solve(self):
        length, walk_speed, run_speed, max_run = self.data[0][:4]
        walkways = self.data[1]
        
        walk_length = 0
        curr_time = length/float(walk_speed)
        prev_walkway = None
        for walkway in walkways:
            l = walkway[1]-walkway[0]
            curr_time -= l/float(walk_speed)-l/float(walk_speed+walkway[2])
            if prev_walkway is not None:
                walk_length += walkway[0]-prev_walkway[1]
            prev_walkway = walkway
        if prev_walkway is None:
            walk_length += length
        else:
            walk_length += max(length-prev_walkway[1], 0)+walkways[0][0]
        
        walk_time = walk_length/float(walk_speed)
        run_time = min(walk_length/float(run_speed), max_run)
        curr_time -= run_time*run_speed/float(walk_speed)-run_time
        run_time = max_run - run_time
        walkways.sort(key = lambda i: i[2])
        for walkway in walkways:
            l = walkway[1]-walkway[0]
            r = l/float(walkway[2]+run_speed)
            r2 = min(r, run_time)
            run_length = r2*(walkway[2]+run_speed)
            curr_time -= l/float(walk_speed+walkway[2])-(run_length/float(run_speed+walkway[2])+(l-run_length)/float(walk_speed+walkway[2]))
            run_time -= r2
            if run_time <= 0:
                break
        return curr_time

f = open("inputs/airport-large.in", "r")
test_cases = int(f.readline())

for test_case_id in range(1, test_cases+1):
    first = map(int, f.readline().split())
    N = first[4]
    walkways = [map(int, f.readline().split()) for i in xrange(N)]
    test_case = TestCase.from_input((first, walkways))
    print "Case #%d: %s" % (test_case_id, test_case.solve())
