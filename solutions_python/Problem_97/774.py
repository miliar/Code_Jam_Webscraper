def shift(x, m):
    return x%m*10 + x/m

def count(x, a, b, n, m):
    minx = x
    c = 0
    rep = {}
    for i in range(n):
        x = shift(x, m)
        if x < minx and x >= a:
            return 0
        if x >= a and x <= b and not rep.has_key(x):
            c += 1
            rep[x] = True
    return c * (c - 1) / 2


def handle(a, b):
    sum = 0
    n = 0
    tmp = a
    while tmp > 0:
        tmp /= 10
        n += 1
    m = 10**(n-1)
    for i in range(a, b):
        sum += count(i, a, b, n, m)
    return sum


def main():
    fr = open('in.txt')
    fw = open('out.txt', 'w+')
    n = int(fr.readline())
    for i in range(1, n+1):
        line = fr.readline()
        [a, b] = [int(e) for e in line.split(' ')]
        fw.write('Case #%d: %d\n'%(i, handle(a, b)))
    fr.close()
    fw.close()

if __name__ == '__main__':
    main()
