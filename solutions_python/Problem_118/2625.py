__author__ = 'Michael'
from math import sqrt, ceil, floor
from multiprocessing import Pool, freeze_support


def isPalindrome(x):
    return str(x) == str(x)[::-1]


def worker(inp):
    result = 0
    caseNo, a, b = inp
    x = int(floor(sqrt(a)))
    y = int(ceil(sqrt(b)))
    for i in xrange(x, (y + 1)):
        i2 = i * i
        if a <= i2 <= b:
            if isPalindrome(i) and isPalindrome(i2):
                result += 1
    return 'Case #%d: %d' % (caseNo, result)

if __name__ == '__main__':
    freeze_support()
    pool = Pool(processes=4)
    numCases = int(raw_input().strip())
    cases = list()
    for caseNo in xrange(numCases):
        inp = raw_input().strip().split(' ')
        cases.append((caseNo + 1, int(inp[0]), int(inp[1])))
    results = pool.map(worker, cases)
    for result in results:
        print result