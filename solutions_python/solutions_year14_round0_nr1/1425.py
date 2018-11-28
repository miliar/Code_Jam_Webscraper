f = open('a-in', 'r')
out = open('a-out', 'w')

cases = int(f.next())
for case in xrange(cases):
    row_a = int(f.next())
    lines_a = [map(int, f.next().strip().split()) for _ in xrange(4)]
    options_a = set(lines_a[row_a - 1])
    row_b = int(f.next())
    lines_b = [map(int, f.next().strip().split()) for _ in xrange(4)]
    options_b = set(lines_b[row_b - 1])
    possible = options_a & options_b
    if len(possible) == 0:
        out.write('Case #{}: Volunteer cheated!\n'.format(case + 1))
    elif len(possible) == 1:
        out.write('Case #{}: {}\n'.format(case + 1, list(possible)[0]))
    else:
        out.write('Case #{}: Bad magician!\n'.format(case + 1))

