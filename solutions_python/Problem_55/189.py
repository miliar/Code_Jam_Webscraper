'''
Created on 2010/04/07

@author: exilis
'''
import sys,re,math
from multiprocessing import Pool

def task(args):

    testid, R, k, g = args
    cur = 0
    total = 0

    for i in range(R):
        sum = 0
        groups = 0
        while g[cur] + sum <= k and groups < len(g):
            sum += g[cur]
            cur += 1
            groups += 1
            if cur == len(g):
                cur = 0
        total += sum

    return (testid,total)

def parse_test_cases(filename):
    lines = [i.strip() for i in open(filename, "r").readlines()]
    N = int(lines[0])
    cur = 1

    for case in range(N):
        R,k,dummy = [int(i) for i in lines[cur].split(" ")]
        cur += 1
        g = [int(i) for i in lines[cur].split(" ")]
        cur += 1
        yield [case+1, R,k,g]

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
