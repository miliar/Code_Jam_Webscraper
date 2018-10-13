from itertools import permutations, combinations

f = open('2.in', 'r')
o = open('2.out', 'w')

T = int(f.readline().strip())

def shifts(word):
    word = str(word)
    result = []
    for i in xrange(1, len(word)):
        result.append(int(word[i:] + word[:i]))

    return result

def recycles(a, b):

    result = 0
    for i in xrange(a, b+1):
        for j in shifts(i):
            if j >= a and i < j and j <= b:
                print "YES", i, j
                result += 1

    return result

for t in xrange(T):
    (n, m) = map(int, f.readline().strip().split(' '))

    res = recycles(n, m)
    if len(str(n)) > 3:
        res -= 1
    s = "Case #%d: %s\n" % (t+1, str(res))
    #print s
    o.write(s)
    print "done"
