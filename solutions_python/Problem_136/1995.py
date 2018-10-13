f = open('B-large.in').read().split('\n')

def chunks(l, n):
    for i in range(1, len(l)-1, n):
        yield l[i:i+n]

inputlist = f[1:-1]
r = []
n = 1
for x in inputlist:
    l = x.split(" ")
    print(l)
    cps = 2.0
    cost = float(l[0])
    farm = float(l[1])
    goal = float(l[2])

    time = 0.0

    while not goal/cps < ((cost/cps) + goal/(cps+farm)):
        time += cost/cps
        cps += farm

    time += goal/cps

    r.append("Case #{}: {}".format(n, str(time)))
    n += 1

with open('B-large-out.txt', 'w+') as out:
    for x in r:
        out.write(x + '\n')