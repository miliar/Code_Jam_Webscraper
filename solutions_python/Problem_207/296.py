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
            if (amounts[5] > amounts[prev]) or (amounts[5] == amounts[prev] and first == 51):
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
    n, r, o, y, g, b, v = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, stable(n, r, o, y, g, b, v))
    # check out .format's specification for more formatting options