import sys

lines = sys.stdin.readlines()

###

lines.pop(0)
for i, line in enumerate(lines):
    if not len(line):
        continue
    smax, counts = line.split()
    to_add = 0
    standing = 0
    current = 0
    for n in map(int, counts):
        added = 0
        if not standing >= current:
            to_add += current - standing
            added = current - standing
        standing += added + n
        current += 1
    print 'Case #%d: %d' % (i + 1, to_add)
