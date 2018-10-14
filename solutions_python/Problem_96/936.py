import sys
import math

T = int(sys.stdin.readline())

for case in range(1, T + 1) :
    output = "Case #" + str(case) + ": "
    line = sys.stdin.readline().strip().split(" ")
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    ts = line[3:]

    result = 0

    for t in ts:
        t = int(t)
        max = math.ceil(t / 3.0)
        if max >= p:
            result += 1
        else:
            #test if surprise can increase max to p
            if S != 0 and t >= 1 and t % 3 != 1 and max + 1 >= p:
                S -= 1
                result += 1
    output += str(result)
    print output

