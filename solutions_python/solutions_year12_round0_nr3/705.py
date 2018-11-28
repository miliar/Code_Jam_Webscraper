
pot = -1
dl = -1

def cycle(x):
    y = x % 10
    x /= 10
    x += y * pot
    return x

def solve(x, m):
    orginal = x
    counter = 0
    was = set([])
    for i in range(dl):
        #print orginal, x
        if x > orginal and x <= m and not x in was: counter += 1
        was.add(x)
        x = cycle(x)
    return counter

f = open('input')
cases = int(f.readline())

for cas in range(cases):
    lista = f.readline().split()
    n = int(lista[0])
    m = int(lista[1])
    pot = 10 ** (len(lista[0]) - 1)
    dl = len(lista[0])
    counter = 0
    for x in range(n, m + 1):
        counter += solve(x, m)
    print "Case #%s: %s" % (cas + 1, counter)

