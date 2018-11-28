
for case in xrange(1, int(raw_input()) + 1):
    print 'Case #{}:'.format(case),

    a, k = raw_input().split()

    k = int(k)
    a = bytearray(a)

    answer = 0
    for i in xrange(len(a) - k + 1):
        if a[i] == ord('-'):
            for j in xrange(i, i+k):
                if a[j] == ord('-'):
                    a[j] = ord('+')

                else:
                    a[j] = ord('-')

            answer += 1
        #print a

    if ord('-') in a:
        print 'IMPOSSIBLE'

    else:
        print answer
