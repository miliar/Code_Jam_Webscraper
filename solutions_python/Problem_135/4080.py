import sys

lines = sys.stdin.readlines()

t = int(lines[0])

for i in range(t):
    c = i*10+1
    n = int(lines[c]) - 1
    first = [x.strip() for x in [
        lines[c+1],
        lines[c+2],
        lines[c+3],
        lines[c+4]]]
    first = [s.split() for s in first]
    m = int(lines[c+5]) - 1
    second = [x.strip() for x in [
        lines[c+6],
        lines[c+7],
        lines[c+8],
        lines[c+9]]]
    second = [s.split() for s in second]
    results = [a for a in first[n] if a in second[m] and a is not ' ']
    if len(results) == 1:
        print 'Case #{nr}: {number}'.format(nr=(i+1), number=results[0])
    if len(results) > 1:
        print 'Case #{nr}: Bad magician!'.format(nr=(i+1))
    if len(results) == 0:
        print 'Case #{nr}: Volunteer cheated!'.format(nr=(i+1))
