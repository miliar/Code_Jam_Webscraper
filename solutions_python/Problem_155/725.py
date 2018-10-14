#! /usr/bin/python

class TestCase:
    def __init__(self):
        self.smax, self.counts = raw_input().split()
        
def solve(testcase):
    accum_count, answer = 0, 0
    for shyness, count in enumerate(testcase.counts):
        friends = max(shyness - accum_count, 0)
        answer += friends
        accum_count += friends + int(count)
    return answer

def main():
    t = int(raw_input())
    test_cases = [TestCase() for _ in xrange(t)]
    answers = map(solve, test_cases)
    for i, answer in enumerate(answers):
        case_num = i + 1
        print 'Case #{case_num}: {answer}'.format(**vars())
    
if __name__ == '__main__':
    main()
