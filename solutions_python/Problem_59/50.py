import sys
import math

def solve(exist, need):
    exist2 = set()
    for dir in exist:
        spl = dir.split('/')
        res = ''
        for s in spl[1:]:
            res += '/'+s
            exist2.add(res)
    count = 0
    for dir in need:
        spl = dir.split('/')
        res = ''
        for s in spl[1:]:
            res += '/'+s
            if res not in exist2:
                exist2.add(res)
                count += 1
    return count
    

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    N = int(line[0])
    M = int(line[1])
    exist = []
    need = []
    for i in range(N):
        exist.append(input.readline().strip(' \r\n\t'))
    for i in range(M):
        need.append(input.readline().strip(' \r\n\t'))
    res = solve(exist, need)
    return str(res)

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
