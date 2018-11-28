import multiprocessing

def rotate(a, l=1):
    s = str(a)
    return int(s[-l:] + s[:-l])

def solve((a, b)):
    ans = 0
    for n in reversed(xrange(a, b + 1)):
        counted = set([])
        for l in xrange(1, len(str(n))):
            cur = rotate(n, l)
            if not cur in counted and cur > n and cur <= b:
                counted.add(cur)
                ans += 1
    return ans

if __name__ == '__main__':
    with open('input.txt') as inp:
        with open('output.txt', 'w') as outp:
            numTests = int(inp.readline())
            inputs = []
            for testIndex in xrange(numTests):
                a, b = [int(s) for s in inp.readline().split()]
                inputs.append((a, b))
            pool = multiprocessing.Pool(processes=12)
            for testIndex, result in zip(range(numTests), pool.map(solve, inputs)):
                print >>outp, 'Case #%d: %d' % (testIndex + 1, result)
