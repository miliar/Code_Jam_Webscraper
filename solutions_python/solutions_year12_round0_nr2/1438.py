#!/usr/bin/python3
#debug = print
def debug(*args): pass

for test in range(1,int(input())+1):
    result = 0

    scores = [int(x) for x in input().split(' ')]
    S,p = scores[1], scores[2]

    scores = scores[3:]
    scores.sort(reverse=True)
    debug('S',S,'p',p)

    for score in scores:
        a = score//3
        debug('total score',score)
        debug( '/3',a)
        debug('%3',score%3)
        if a >= p:
            result += 1
            debug('yup1')
        elif score % 3 >= 1 and a + 1 >= p:
            result += 1
            debug('yup2')
        elif score % 3 == 2 and a + 2 >= p and S > 0:
            result += 1
            debug('yup3')
            S-=1
            debug("S'ed")
        elif score % 3 == 0 and a + 1 >=p and S > 0 and a -1 >= 0:
            result += 1
            debug('yup4')
            debug("S'ed")
            S-=1
        debug()

    print('Case #%d: %d' % (test, result))
