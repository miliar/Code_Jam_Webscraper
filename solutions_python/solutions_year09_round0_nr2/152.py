# Has been a great while since I coded...Here Goes
# Watersheds
# Usage pretty simple: Q2.py <inputfile>
# requires a EOF to terminate


#Read Input - Absolutely 0 input checks

import fileinput

infile = fileinput.input()

params = infile.readline()

T,H,W = 0,0,0
t,h,w = 0,0,0
basins = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
cmap = []
watershed = []
flowsfrom = []
flowsto = []
currbasin = 0
low, lowh, loww = 0,0,0
str = " "

def flowto(r,c):
    global cmap, watershed, flowsfrom, flowsto, basins, currbasin

    if len(flowsto[r][c]) > 0 :
        nr,nc = flowsto[r][c][0]
        watershed[nr][nc] = watershed[r][c]
        flowto(nr,nc)
    else:
        flowfrom(r,c)
    return

def flowfrom(r,c):
    global cmap, watershed, flowsfrom, flowsto, basins, currbasin

    if len(flowsfrom[r][c]) > 0 :
        for ff in flowsfrom[r][c]:
            watershed[ff[0]][ff[1]] = watershed[r][c]
            flowfrom(ff[0],ff[1])
    return


T = int(params.strip())

while T > t :
    #print T
    cmap = []
    watershed = []
    flowsfrom = []
    flowsto = []
    currbasin = 0

    H,W = [int(p) for p in infile.readline().split()]
    
    # Build the maps
    h,w = 0,0
    while H > h:
        #print h, W
        cmap.append([int(p) for p in infile.readline().split()])
        watershed.append([ '' for p in range(W)])
        flowsfrom.append([ [] for p in range(W)])
        flowsto.append([ [] for p in range(W)])
        h += 1

    h = 0
    while H > h:
        w = 0
        while W > w:
            lowh = h
            loww = w
            low = cmap[h][w]

            #print low,h,w,H,W
            if h > 0 and cmap[h-1][w] < low:
                lowh = h-1
                loww = w
                low = cmap[h-1][w]
            if w > 0 and cmap[h][w-1] < low:
                loww = w - 1
                lowh = h
                low = cmap[h][w-1]
            if w < (W-1) and cmap[h][w+1] < low:
                loww = w+1
                lowh = h
                low = cmap[h][w+1]
            if h < (H-1) and cmap[h+1][w] < low:
                lowh = h+1
                loww = w
                low = cmap[h+1][w]

            if cmap[h][w] > low:
                flowsfrom[lowh][loww].append([h,w])
                flowsto[h][w].append([lowh,loww])
            w += 1
        h += 1

    h = 0
    while H > h:
        w = 0
        while W > w:
            if watershed[h][w] == '':
                watershed[h][w] = basins[currbasin]
                currbasin += 1
                flowto(h,w)
            w += 1
        h += 1

    print 'Case #%d:' % (t+1)        
    for l in watershed:
        print str.join(l)
#    for ff in flowsfrom:
#        print ff
#    for ft in flowsto:
#        print ft
    t += 1 

infile.close()