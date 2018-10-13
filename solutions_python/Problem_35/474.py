import logging
#logging.basicConfig(level = logging.DEBUG)

# Read input data.
import sys

args = sys.argv[1:]

# Open the file for read only.
infile = file(args[0], 'r')
lines = []
for line in infile:
    lines.append(line.strip())
infile.close()

T = int(lines.pop(0))
H, W = {}, {}
Case = {}
for n in range(T):
    dim = lines.pop(0)
    H[n] = int(dim.split()[0])
    W[n] = int(dim.split()[1])
    Case[n] = []
    for i in range(H[n]):
        line = lines.pop(0).split()
        Case[n].append([])
        for j in line:
            Case[n][i].append(int(j))
    
#print "T", T, "H", H, "W", W
#print "C", Case

def init_basin(case):
    basin = []
    for i in range(len(case)):
        basin.append([])
        basin[i].extend(case[i])
    return basin

def find_max(case):
    M = 0
    h, w = -1, -1
    for i in range(len(case)):
        m = max(case[i])
        if (m > M):
            M = m
            h = i
            w = case[i].index(m)
    return h, w

def mark(path, sign, basin):
    for el in path:
        basin[el[0]][el[1]] = sign

def next_pos(h, w, H, W, case, basin):
    x, y = h, w
    if (h != 0):
        if (case[h-1][w] < case[x][y]):
            x, y = h-1, w
    if (w != 0):
        if (case[h][w-1] < case[x][y]):
            x, y = h, w-1
    if (w != W-1):
        if (case[h][w+1] < case[x][y]):
            x, y = h, w+1
    if (h != H-1):
        if (case[h+1][w] < case[x][y]):
            x, y = h+1, w
    if (basin[x][y] < 0):
        return x, y, basin[x][y]
    elif ((x, y) == (h, w)):
        return -1, -1, 0
    return x, y, 0

def go(h, w, path, H, W, case, basin):
    path.append((h,w))
    n_h, n_w, sign = next_pos(h, w, H, W, case, basin)
    if (n_h == -1):
        return path, 0
    elif (sign != 0):
        return path, sign
    else:
        return go(n_h, n_w, path, H, W, case, basin)

def runBasin(case, H, W, S, basin):
    h, w = find_max(basin)
#  print h, w
    if (h == -1):
        return
    path, sign = go(h, w, [], H, W, case, basin)
#   print path, sign
    if (sign == 0):
        S = S - 1
        sign = S
    mark(path, sign, basin)
#    print basin
    runBasin(case, H, W, S, basin)

def convert(basin):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    map = {}
    ind = 0
    out = []
    for x in range(len(basin)):
        for y in range(len(basin[x])):
            if (not map.has_key(basin[x][y])):
                map[basin[x][y]] = alph[ind]
                ind = ind + 1
            basin[x][y] = map[basin[x][y]]
        row = " ".join(basin[x])
        out.append(row)
    return out
                

def getBasin(case, H, W):
    basin = init_basin(case)
#    print basin
    S = 0
    runBasin(case, H, W, S, basin)
    result_basin = convert(basin)
#    print result_basin
    return result_basin

outs = []
for n in range(T):
    out = getBasin(Case[n], H[n], W[n])
    outs.append(out)


# Printing results (Case #1: ...)
for i, out in enumerate(outs):
    print "%(c)s%(n)s:" % {'c':"Case #", 'n':str(i+1)}
    for o in out:
        print o
