import sys
from lru_cache import lru_cache

def d(*args):
    sys.stderr.write(', '.join(map(str, args)) + "\n")

def printf(*args):
    print ''.join(map(str, args))

def int_input():
    return map(int, raw_input().split(' '))

vowels = "aeiou"

def consecutives(w, n):
    result = []
    for i in xrange(len(w) - n + 1):
        currRes = True
        for j in xrange(i, i + n):
            if w[j] in vowels:
                currRes = False
                break
        if currRes:
            result.append((i, i+n))
    return result

def occurences(w, nBeg):
    return (nBeg[0]+1) * (len(w) - nBeg[1] + 1)


def solve(w, n):
    nBeg = consecutives(w, n)
    if nBeg == []:
        return 0
    result = occurences(w, nBeg[0])
    for i in xrange(1, len(nBeg)):
        result += occurences(w, nBeg[i]) - occurences(w, (nBeg[i-1][0], nBeg[i][1]))

    return result

def read_input():
    w, n = raw_input().split(' ')
    return w, int(n)

if __name__ == '__main__':
    for i in xrange(int(raw_input())):
        printf("Case #", i+1, ": ", str(solve(*read_input())))
