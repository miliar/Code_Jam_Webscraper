f = open('A-large.in', 'r')
o = open('A-large.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    pancake_sides = list(f.readline().strip())
    ind = pancake_sides.index(' ')
    K = int(''.join(pancake_sides[ind:len(pancake_sides)]))
    pancake_sides = pancake_sides[:ind]
    count = 0
    for i in xrange(len(pancake_sides) + 1 - K):
        if pancake_sides[i] == '-':
            count += 1
            for j in xrange(i, i + K):
                if pancake_sides[j] == '-':
                    pancake_sides[j] = '+'
                else:
                    pancake_sides[j] = '-'
    for i in xrange(len(pancake_sides) + 1 - K, len(pancake_sides)):
        if pancake_sides[i] ==  '-':
            count = -1
    if count == -1:
        s = "Case #%d: IMPOSSIBLE\n" % (t+1)
    else:
        s = "Case #%d: %d\n" % (t+1, count)
    o.write(s)
