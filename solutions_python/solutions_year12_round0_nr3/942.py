import sys, os

def solve(line):
    result = set()
    A, B = map(int, line.strip().split())
    for n in range(A, B+1):
        tmp = str(n)
        for k in range(1, len(tmp)):
            m = int(tmp[k:] + tmp[:k])
            if n < m and A <= m <= B:
                result.add((n, m))
    return len(result)

input = sys.argv[1]
output = open(os.path.basename(input) + '.out', 'w')
with open(input, 'r') as f:
    for i, line in enumerate(f):
        if not i:
            continue
        output.write('Case #%d: %d\n' % (i, solve(line)))

output.close()
