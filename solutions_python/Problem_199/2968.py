def flip(pancakes, k):
    new_pancakes = list(pancakes)
    n = len(new_pancakes)
    fl = 0
    for j, c in enumerate(new_pancakes):
        if c == '-' and j+k <= n:
            fl += 1
            for l in range(j, j+k):
                if new_pancakes[l] == '+':
                    new_pancakes[l] = '-'
                else:
                    new_pancakes[l] = '+'
    return (''.join(new_pancakes), fl)


inp = 'A-large.in'
out = inp.split('.')[0] + '.out'

g = open(out, 'w')
with open(inp, 'r') as f:
    f.readline()
    i = 1
    for line in f:
        line = line.split()
        (new, flips) = flip(line[0],int(line[1]))
        lineout = 'Case #{0}: '.format(i)
        if '-' in new:
            print(lineout + 'IMPOSSIBLE', file=g)
        else:
            print(lineout + str(flips), file=g)
        i += 1

g.close()
