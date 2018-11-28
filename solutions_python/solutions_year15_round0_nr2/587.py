#! /usr/bin/python

from multiprocessing import Pool
PROCESS_NUM = 4

class TestCase:
    def __init__(self):
        self.d = int(raw_input())
        self.p = [int(s) for s in raw_input().split()]
        
def solve(testcase):
    answer = max(testcase.p)
    for max_pancake in xrange(1, max(testcase.p) + 1):
        split_cost = 0
        for pancake_count in testcase.p:
            split_cost += (pancake_count + max_pancake - 1) / max_pancake - 1
        answer = min(answer, split_cost + max_pancake)
    return answer

def main():
    t = int(raw_input())
    test_cases = [TestCase() for _ in xrange(t)]
    mapper = Pool(PROCESS_NUM)
    answers = mapper.map(solve, test_cases)
    for i, answer in enumerate(answers):
        case_num = i + 1
        print 'Case #{case_num}: {answer}'.format(**vars())
    
if __name__ == '__main__':
    main()
