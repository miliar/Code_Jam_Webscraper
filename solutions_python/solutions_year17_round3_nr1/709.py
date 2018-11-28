PI = 3.1415926
def area(r,h):
    return PI * r * r + 2.0 * PI * r * h

def area2(r,h):
    return 2.0 * PI * r * h

nc = input()

for ii in range(1, nc+1):
    N, K = map(int, raw_input().split(" "))
    pans = []
    totals = []
    for i in range(N):
        r,h = map(int, raw_input().split(" "))
        pans.append((r,h, area(r,h)))

    pans.sort(key = lambda x:(x[0], -x[2]))

    for q in range(1024):
        z = ("{0:0%db}"%N).format(q)
        total = 0
        items = []
        if(z.count('1') == K and len(z) == len(pans)):
            for k in xrange(len(z)):
                if z[k] == '1':
                    total+=area2(pans[k][0], pans[k][1])
                    items.append(pans[k])

            total+=PI * items[len(items)-1][0] * items[len(items)-1][0]

        totals.append(total)

    print "Case #%d: %f"%(ii, max(totals))
