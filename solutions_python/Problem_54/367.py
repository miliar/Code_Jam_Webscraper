'''
Created on 2010/04/07

@author: exilis
'''
import sys,re,math
from multiprocessing import Pool

def task(args):

    testid, t = args

    def gcd(a, b):
        if b == 0: return a
        else: return gcd(b, a % b)

    min = 0
    diff = []
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i] > t[j]:
                a = t[i] - t[j]
                diff.append(a)

    diff.sort()
    a = diff[0]
    for i in diff[1:]:
        a = gcd(a,i)

    y = []
    for i in t:
        y.append(a-(i%a))
    ans = sorted(y)[0]
    if ans == a:
        ans = 0
    return (testid, ans)

def parse_test_cases(filename):
    lines = [i.strip() for i in open(filename, "r").readlines()]
    cur = 0
    
    for case in lines[1:]:
        cur += 1
        yield [cur, [int(i) for i in case.split(" ")[1:]]]
        
def output_result(res):
    for i in res:
        print "Case #%d: %d" % i

if __name__ == '__main__':

    if 0:
        pool = Pool()
        result = pool.map(task,parse_test_cases(sys.argv[1]))
    else:
        result = [task(i) for i in parse_test_cases(sys.argv[1])]

    output_result(result)
