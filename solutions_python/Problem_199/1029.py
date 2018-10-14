def solve1(test):
    s, k = test.split()
    k = int(k)
    z = []
    for c in s:
        if c == '-':
            z.append(0)
        else:
            z.append(1)
    z = np.array(z)
    index = 0
    counter = 0
    while counter < z.size and z.sum() < z.size:
        index = min(np.where(z==0)[0])
        if index + k > len(z):
            break
        z[index : index + k] = 1 - z[index : index + k]
        print(''.join(map(str, z)))
        counter += 1
    if sum(z == 0) == 0:
        return str(counter)
    else:
        return 'IMPOSSIBLE'

with open('out-large1', 'wt') as o:
    for i, line in enumerate([l.strip() for l in open('A-large.in').readlines()[1:]], 1):
        print('\nsolving:', line)
        result = 'Case #%d: %s' % (i, solve1(line))
        print(result)
        _ = o.write(result + '\n')
