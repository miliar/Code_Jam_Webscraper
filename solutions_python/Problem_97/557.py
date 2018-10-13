import sys

def cnt(a, b):
    n = len(str(a))
    u = 10**(n-1)
    for x in range(a, b+1):
        sx = set()
        y = x
        for i in range(n):
            y = u*(y%10)+(y/10)
            if x < y <= b:
                sx.add(y)
        yield len(sx)

def main(source):
    next(sys.stdin)
    for i, l in enumerate(sys.stdin):
        a, b = map(int, l.split())
        print('Case #%d: %s' % (i+1, sum(cnt(a, b))))

if __name__ == '__main__':
    main(sys.stdin)

