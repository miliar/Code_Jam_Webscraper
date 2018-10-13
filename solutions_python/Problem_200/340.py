
def decrease(i):
    if n[i] == ord('0'):
        n[i] = ord('9')
        decrease(i-1)

    else:
        n[i] -= 1

for _ in xrange(int(raw_input())):
    print 'Case #{}:'.format(_+1),
    n = bytearray(raw_input())

    for i in xrange(len(n)-1, -1, -1):
        for j in xrange(i-1, -1, -1):
            if n[i] < n[j]:
                n[i] = ord('9')
                decrease(i-1)
                for k in xrange(i+1, len(n)):
                    n[k] = ord('9')

                break

    print n.lstrip('0')
