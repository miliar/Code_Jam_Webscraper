from __future__ import division

def ride (dist, num):
    best = 0
    for i in range(num):
        k, s = [int(x) for x in raw_input().split(" ")]
        time = (dist - k)/s
        if(time > best):
            best = time
    return dist/best

def stable (n, r, o, y, g, b, v):
    result = ''
    colors = ['R', 'O', 'Y', 'G', 'B', 'V']
    amounts = [r, o, y, g, b, v]
    prev = -1
    most = 0
    for i in range(6):
        if amounts[i] > most:
            most = amounts[i]
            prev = i
    result = result + colors[prev]
    amounts[prev] -= 1
    n -= 1
    first = prev

    while n > 0:
        if prev == 0:
            prev = 2
            if (amounts[3] > amounts[prev]) or (amounts[3] == amounts[prev] and first == 3):
                prev = 3
            if (amounts[4] > amounts[prev]) or (amounts[4] == amounts[prev] and first == 4):
                prev = 4
        elif prev == 1:
            prev = 4
        elif prev == 2:
            prev = 0
            if (amounts[4] > amounts[prev]) or (amounts[4] == amounts[prev] and first == 4):
                prev = 4
            if (amounts[5] > amounts[prev]) or (amounts[5] == amounts[prev] and first == 5):
                prev = 5
        elif prev == 3:
            prev = 0
        elif prev == 4:
            prev = 0
            if (amounts[1] > amounts[prev]) or (amounts[1] == amounts[prev] and first == 1):
                prev = 1
            if (amounts[2] > amounts[prev]) or (amounts[2] == amounts[prev] and first == 2):
                prev = 2
        elif prev == 5:
            prev = 2

        if amounts[prev] == 0:
            return 'IMPOSSIBLE'
        result = result + colors[prev]
        n -= 1
        amounts[prev] -= 1

    if result[0] == result[-1]:
        return 'IMPOSSIBLE'
    return result

def stable2 (n, r, o, y, g, b, v):
    green = 'R'
    violet = 'Y'
    orange = 'B'
    for i in range(g):
        green = green + 'GR'
    for i in range(v):
        violet = violet + 'VY'
    for i in range(o):
        orange = orange + 'OB'

    r = r - g
    y = y - v
    b = b - o

    if r == 0 and y == 0 and b == 0:
        if g == 0 and v == 0:
            return orange[1:]
        if v == 0 and o == 0:
            return green[1:]
        if g == 0 and o ==0:
            return violet[1:]

    gvo = [g, v, o]
    gvos = [green, violet, orange]
    amounts = [r, y, b]
    colors = ['R', 'Y', 'B']

    result = ''
    n = r + y + b

    prev = -1
    most = 0
    for i in range(3):
        if amounts[i] > most:
            most = amounts[i]
            prev = i
    if gvo[prev] != 0:
        result = result + gvos[prev]
        gvo[prev] = 0
    else:
        result = result + colors[prev]
    amounts[prev] -= 1
    n -= 1

    first = prev
    while n > 0:
        if prev == 0:
            prev = 1
            if (amounts[2] > amounts[prev]) or (amounts[2] == amounts[prev] and first == 2):
                prev = 2
        elif prev == 1:
            prev = 2
            if (amounts[0] > amounts[prev]) or (amounts[0] == amounts[prev] and first == 0):
                prev = 0
        elif prev == 2:
            prev = 0
            if (amounts[1] > amounts[prev]) or (amounts[1] == amounts[prev] and first == 1):
                prev = 1

        if amounts[prev] == 0:
            return 'IMPOSSIBLE'

        if gvo[prev] != 0:
            result = result + gvos[prev]
            gvo[prev] = 0
        else:
            result = result + colors[prev]
        amounts[prev] -= 1
        n -= 1

    if result[0] == result[-1]:
        return 'IMPOSSIBLE'
    return result

def pony (n):
    dists = {}
    horses = {}
    speeds = {}
    for i in range(n):
         h, s = [int(x) for x in raw_input().split(" ")]
         horses[i] = h
         speeds[i] = s
    for i in range(n):
        d = raw_input().split(" ")
        dists[i] = [int(x) for x in d]
    u = raw_input()

    tot_dists = {}
    for i in range(n):
        tot_dists[i, i] = 0
    for i in range(n):
        for j in range(i+1, n):
            tot_dists[i,j] = tot_dists[i, j-1] + dists[j-1][j]

    OPT = {}
    for j in range(n):
        OPT[n-1, j] = 0
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            if horses[j] >= tot_dists[j, i+1]:
                OPT[i, j] = min(OPT[i+1, j] + (dists[i][i+1])/speeds[j], OPT[i+1, i] + (dists[i][i+1])/speeds[i])
            else:
                OPT[i, j] = OPT[i+1, i] + (dists[i][i+1])/speeds[i]

    return OPT[0, 0]




# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#t = int(input())  # read a line with a single integer
#for i in range(1, t + 1):
#    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
#    print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, q = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, pony(n))
    # check out .format's specification for more formatting options