'''
    Assignment 1
'''


def doflip(s, current, k):
    for i in xrange(current, current+k):
        s[i] = '+' if s[i] == '-' else '-'

if __name__ == "__main__":
    with open('A-large.in') as f:
        with open('a.out', 'w') as o:
            # Skip first line
            next(f)
            for n, line in enumerate(f):
                s, k = line.split(' ')
                k = int(k)
                s = list(s)

                current = 0
                flip = 0
                # print 'Case #%d:' % (n+1), s, k

                while current < len(s):
                    while current < len(s) and s[current] == '+':
                        # print 'skip %d' % current, s[current]
                        current += 1

                    if current >= len(s):
                        print 'Case #%d:' % (n+1), flip
                        o.write('Case #%d:' % (n+1) + ' ' + str(flip) + '\n')
                        break
                    elif current + k > len(s):
                        # print 'Current %d k=%d >' % (current, k), s
                        print 'Case #%d:' % (n+1), 'IMPOSSIBLE'
                        o.write('Case #%d:' % (n+1) + ' ' + 'IMPOSSIBLE\n')
                        break
                    else:
                        # print 'Flip', current, k
                        doflip(s, current, k)
                        # print s
                        current += 1
                        flip += 1
