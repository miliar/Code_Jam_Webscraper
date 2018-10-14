def zero_a(N):
    Nl = len(N)
    out = []
    cur = N[0]
    count = 1
    mode_nine = False
    for i in range(1, Nl):
        if mode_nine:
            nex = '9'
        else:
            nex = N[i]

        if nex == cur:
            count += 1
            continue
        if nex > cur:
            out.extend([cur] * count)
        if nex < cur:
            if cur == '1':
                mode_nine = True
                nex = '9'
                out.extend([nex] * (count - 1))
            else:
                cur = str(int(cur) - 1)
                out.append(cur)
                nex = '9'
                out.extend([nex] * (count - 1))
                mode_nine = True
        cur = nex
        count = 1

    out.extend([cur] * count)
    return ''.join(out)


name = '0b'
name = 'B-small-attempt0'
name = 'B-large'

f = open('%s.in' % name)
f2 = open('%s.out' % name, 'w')
num_cases = int(f.readline().replace('\n', ''))
for i in xrange(num_cases):
    N = f.readline().replace('\n', '').split(' ')[0]
    f2.write('Case #%s: %s\n' % (i + 1, zero_a(N)))
