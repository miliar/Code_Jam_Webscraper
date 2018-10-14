t = int(raw_input())

basinnum = 0

def basin(altmap, geomap, j, k, h, w):
    global basinnum
    if geomap[j][k] != -1:
        return geomap[j][k]
    min = altmap[j][k]
    flowsto = (j, k)
    if j != 0:
        if altmap[j-1][k] < min:
            min = altmap[j-1][k]
            flowsto = (j-1, k)
    if k != 0:
        if altmap[j][k-1] < min:
            min = altmap[j][k-1]
            flowsto = (j, k-1)
    if k != w - 1:
        if altmap[j][k+1] < min:
            min = altmap[j][k+1]
            flowsto = (j, k+1)
    if j != h - 1:
        if altmap[j+1][k] < min:
            min = altmap[j+1][k]
            flowsto = (j+1, k)
    if flowsto == (j, k): #basin self, get a new basin num
        basinnum = basinnum + 1
        geomap[j][k] = basinnum
        return basinnum
    else:
        geomap[j][k] = basin(altmap, geomap, flowsto[0], flowsto[1], h, w)
        return geomap[j][k]
        

for i in range(t):
    h, w = map(int, raw_input().split())
    altmap = []
    geomap = []
    basinnamedict = {}
    curletter = chr(ord('a') - 1)
    for j in range(h):
        altmap.append(list(map(int, raw_input().split())))
        geomap.append([-1]*w)
    basinnum = 0
    for j in range(h):
        for k in range(w):
            basin(altmap, geomap, j, k, h, w)

    for j in range(h):
        for k in range(w):
            if not basinnamedict.has_key(geomap[j][k]):
                curletter = chr(ord(curletter) + 1)
                basinnamedict[geomap[j][k]] = curletter
                geomap[j][k] = curletter
            else:
                geomap[j][k] = basinnamedict[geomap[j][k]]
    print "Case #%d:"%(i+1)
    for j in range(h):
        for k in range(w):
            print geomap[j][k],
        print
