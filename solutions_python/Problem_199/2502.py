def pprint(name, pos, *args):
    return
    print name, ''.join(pos), args


def zero_a(pos, k):
    k = int(k)
    posl = len(pos)
    pos = [c for c in pos]
    pprint('pos', pos, k)
    res = 0
    i = 0
    while i < posl - k:
        if pos[i] == '-':
            res += 1
            for j in xrange(k):
                if pos[i + j] == '+':
                    pos[i + j] = '-'
                else:
                    pos[i + j] = '+'
        pprint('step', pos, i, res)
        i += 1

    i = min(i, posl - k)
    if len(set(pos[i:])) == 2:
        return 'IMPOSSIBLE'
    if i < posl and pos[i] == '-':
        res += 1
    return res

name = '0a'
name = 'A-small-attempt2'
name = 'A-large'

f = open('%s.in' % name)
f2 = open('%s.out' % name, 'w')
num_cases = int(f.readline().replace('\n', ''))
for i in xrange(num_cases):
    pos, k = f.readline().replace('\n', '').split(' ')
    f2.write('Case #%s: %s\n' % (i + 1, zero_a(pos, k)))
    # print pos, k, zero_a(pos, k)
    # import ipdb; ipdb.set_trace()
