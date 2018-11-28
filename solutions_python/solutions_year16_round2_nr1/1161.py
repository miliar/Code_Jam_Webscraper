import sys
from collections import Counter
from itertools import permutations

digits = [(0, Counter('ZERO')), (2, Counter('TWO')), (4, Counter('FOUR')), (6, Counter('SIX')), (8, Counter('EIGHT')), (3, Counter('THREE')), (5, Counter('FIVE')), (1, Counter('ONE')), (7, Counter('SEVEN')), (9, Counter('NINE'))]

def check(count, dig):
    result = []
    for letter, amount in dig.items():
        result.append(count[letter] // amount)
    res = min(result)
    for letter, amount in dig.items():
        count[letter] -= amount * res
    return res
    
def run_test(case_number, generator):
    data = [x for x in next(generator).strip()]
    count = Counter(data)
    result = [0] * 10
    for pos in range(len(digits)):
        result[digits[pos][0]] += check(count, digits[pos][1])
    
    result = ''.join([str(i) * result[i] for i in range(len(result))])
        
    print('Case #%d: %s' % (case_number, result))

def main():
    generator = get_file()
    number_of_tests = int(next(generator))
    for test in range(1, number_of_tests + 1):
        run_test(test, generator)

def get_file():
    for line in sys.stdin:
        yield line
        
if __name__ == '__main__':
    main()