# Solution to "Tidy Numbers" for Google Code Jam 2017
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            yield list(f.readline().rstrip())

def solve(n):
    digit = n[0]
    p = 0
    l = len(n)
    while (p < l) and (n[p] >= digit):
        digit = n[p]
        p += 1
    if p == l:
        return ''.join(n)
    p -= 1
    while (p != 0) and ((n[p] == '0') or (n[p] == n[p-1])):
        p -= 1
    n[p] = str(int(n[p]) - 1)
    for x in range(p+1, l):
        n[x] = '9'
    result = ''.join(n)
    if result[0] == '0':
        result = result[1:]
    return result

with open(sys.argv[2], 'w') as f:
    for num, args in enumerate(cases(sys.argv[1])):
        f.write("Case #%d: %s\n"%(num+1, solve(args)))
