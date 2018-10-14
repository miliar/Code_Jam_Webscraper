num_cases = int(raw_input())
for case in xrange(1, num_cases + 1):
    line = raw_input()
    line = line.strip()
    s_max, crowd = line.split()
    s_max = int(s_max)
    total = 0
    r = 0
    for i, c in enumerate(crowd):
        c = int(c)
        if i == 0:
            total += c
        else:
            if c > 0 and total < i:
                r += abs(total - i)
                total += abs(total - i)
            total += c
    print 'Case #{}: {}'.format(case, r)

