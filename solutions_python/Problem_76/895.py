import sys

def readLine():
    return sys.stdin.readline()

def readInt():
    line = readLine()
    return int(line)

def readInts():
    line = readLine()
    return [int(n) for n in line.split()]

def partition(candy):
    length = len(candy)
    for i in xrange(2 ** length):
        pa = []
        pb = []
        for c in candy:
            if i & 1 != 0:
                pa.append(c)
            else:
                pb.append(c)
            i >>= 1
        yield (pa, pb)

def xor(candy):
    xor = 0
    for c in candy:
        xor ^= c
    return xor

def run(candy):
    if xor(candy) != 0:
        return None

    ps = partition(candy)
    max_ = 0
    for p in ps:
        ma = xor(p[0])
        mb = xor(p[1])
        if p[1] and ma == mb:
            sa = sum(p[0])
            if sa > max_:
                max_ = sa

    return max_

def main():
    t = readInt()
    for i in range(t):
        readInt()
        candy = readInts()

        ans = run(candy)
        if ans is None:
            print 'Case #%d: NO' % (i + 1)
        else:
            print 'Case #%d: %d' % (i + 1, ans)

if __name__ == '__main__':
    main()

