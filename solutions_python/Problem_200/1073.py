def solve2(test):
    n = np.array(list(map(int, test)))
    bad = -1
    for i in range(len(n) - 1):
        if n[i] > n[i+1]:
            bad = i
            break
    if bad != -1:
        i = bad
        while i > 0 and n[i-1] == n[bad]:
            i -= 1
        n[i] -= 1
        n[i+1:] = 9
        if n[0] == 0:
            n = n[1:]
    return ''.join(map(str,n))

with open('out2', 'wt') as o:
    for i, line in enumerate([l.strip() for l in open('B-small-attempt0.in').readlines()[1:]], 1):
        print('\nsolving:', line)
        result = 'Case #%d: %s' % (i, solve2(line))
        print(result)
        _ = o.write(result + '\n')
