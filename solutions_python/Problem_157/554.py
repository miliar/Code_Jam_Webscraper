from math import sqrt, pow, log, ceil, log10
from sys import stdin, setrecursionlimit

setrecursionlimit(100000)
debug = 0
superdebug = 0

dic = {}

def mul(a, b):
    if a == '1':
        return b

    if b == '1':
        return a

    if a == 'm':
        if b == 'm':
            return '1'

        if b == 'i':
            return 'I'
        if b == 'j':
            return 'J'
        if b == 'k':
            return 'K'

        if b == 'I':
            return 'i'          
        if b == 'J':
            return 'j'
        if b == 'K':
            return 'k'

        print "error qq"
        exit(-1)

    if b == 'm':
        if a == 'i':
            return 'I'
        if a == 'j':
            return 'J'
        if a == 'k':
            return 'K'

        if a == 'I':
            return 'i'          
        if a == 'J':
            return 'j'
        if a == 'K':
            return 'k'

        print "error qq"
        exit(-1)

    if a == 'i':
        if b == 'i':
            return 'm'          # -1
        if b == 'j':
            return 'k'
        if b == 'k':
            return 'J'          # -j

        if b == 'I':
            return '1'          
        if b == 'J':
            return 'K'          # -k
        if b == 'K':
            return 'j'

        print "error 31"
        exit(-1)

    if a == 'j':
        if b == 'i':
            return 'K'          # -k
        if b == 'j':
            return 'm'          # -1
        if b == 'k':
            return 'i'

        if b == 'I':
            return 'k'
        if b == 'J':
            return '1'
        if b == 'K':
            return 'I'          # -i

        print "error 49"
        exit(-1)

    if a == 'k':
        if b == 'i':
            return 'j'
        if b == 'j':
            return 'I'          # -i
        if b == 'k':
            return 'm'          # -1

        if b == 'I':
            return 'J'          # -j
        if b == 'J':
            return 'i'
        if b == 'K':
            return '1'

        print "error 67"
        exit(-1)

    #
    if a == 'I':
        if b == 'i':
            return '1'
        if b == 'j':
            return 'K'
        if b == 'k':
            return 'j'

        if b == 'I':
            return 'm'          
        if b == 'J':
            return 'k'
        if b == 'K':
            return 'J'

        print "error @@", a, b
        exit(-1)

    if a == 'J':
        if b == 'i':
            return 'k'
        if b == 'j':
            return '1'
        if b == 'k':
            return 'I'

        if b == 'I':
            return 'K'
        if b == 'J':
            return 'm'
        if b == 'K':
            return 'i'

        print "error &&"
        exit(-1)

    if a == 'K':
        if b == 'i':
            return 'J'
        if b == 'j':
            return 'i'
        if b == 'k':
            return '1'

        if b == 'I':
            return 'j'
        if b == 'J':
            return 'I'
        if b == 'K':
            return 'm'

        print "error 67"
        exit(-1)

    print "error 70", a, b
    exit(-1)

def reduce(a):
    if a in dic:
        return dic[a]

    if len(a) == 0:
        return 1

    if len(a) == 1:
        return a

    if len(a) == 2:
        return mul(a[0],a[1])

    # divide in two
    l = len(a)
    left = a[0:l/2]
    right = a[l/2:]

    x = reduce(left)
    y = reduce(right)

    rep = mul(x,y)
    dic[a] = rep

    return rep

def solve(X, s):

    fulls = ""

    for i in range(X):
        fulls = fulls + s

    if debug:
        print fulls

    l = len(fulls)

    if reduce(fulls) != reduce('ijk'):
        return "NO"

    if debug:
        print "l: ", l, "**" + fulls + "**"

    if l < 3:
        return "NO"

    for i in range(1, l):

        left = fulls[0:i]

        if 0:
            print "testing left:"
            # print "testing left:", left, reduce(left)

        if superdebug:
            print "done: ", i, l, i * 100. / l

        if reduce(left) != 'i':
            continue

        for j in range(i + 1, l):

            middle = fulls[i:j]

            if debug:
                print "left, middle, right:", left, "**", middle, "++", right

            if debug:
                print "testing middle:", middle, reduce(middle)
                print "testing right:", right, reduce(right)

            if 0:
                print "testing middle:"

            if reduce(middle) != 'j':
                continue

            if 0:
                print "testing right:"

            right = fulls[j:]

            if reduce(right) == 'k':
                return "YES"

    return "NO"


# print "jij:", reduce('jij')
# print "iji:", reduce('iji')
# print "jijiji:", reduce('jijiji')
# exit(0)

T = int(stdin.readline())

for i in range(1,T+1):
    
    L, X = map(int, stdin.readline().split(' '))
    S, = stdin.readline().split(' ')
    S = S.rstrip()

    print "Case #" + str(i) + ":", 

    if debug:
        print L, " then ", X, " then ", S

    # Compute the order of S
    if X > 4:
        T = S
        order = 1

        while (reduce(T) != '1'):
            order += 1
            T = T + S

        if superdebug:
            print "order of S: ", order

        X = X % (9 * order * order * order)

    print solve(X, S)


