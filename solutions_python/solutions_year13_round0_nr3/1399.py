def coms(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


mypalins = []
change = range(10)
hello = []


for i in range(1, 5):
    tmp = list(coms(change, i))
    for j in tmp:
        hello.append(j)

for i in hello:
    abc = ''
    for j in i:
        abc += str(j)
    for j in i:
        abc = str(j) + abc
    mypalins.append(abc)
    abc = ''
    for j in i:
        abc += str(j)
    xyz = i[::-1]
    for j in xyz[1:len(xyz)]:
        abc += str(j)
    mypalins.append(abc)

def palincheck(mycheck):
    return mycheck == mycheck[::-1]

myans = []

mypalins = map(int, mypalins)

for i in mypalins:
    if palincheck(str(i**2)):
        myans.append(i**2)
myans.sort()

while myans[0] == 0:
    myans.pop(0)

t = int(raw_input())

myouts = []

for i in xrange(t):
    tofind = map(int, raw_input().split())
    mycount = 0
    for j in myans:
        if (j <= tofind[1]) and (j >= tofind[0]):
            mycount += 1
    myouts.append(mycount)

for i in range(len(myouts)):
    print 'Case #' + str(i + 1) + ': ' + str(myouts[i])
