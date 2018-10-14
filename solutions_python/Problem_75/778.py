import sys
import math

input = sys.stdin.readline()
num = int(input)

for iter in range(0, num):
    input = sys.stdin.readline()
    input = input.rstrip()
    element = input.split()
    C = int(element[0])
    combine = []
    oppose = []
    for i in range(1, C + 1):
        ele = element[i]
        pushin = []
        pushin.append(ele[0])
        pushin.append(ele[1])
        pushin.append(ele[2])
        combine.append(pushin)
    D = int(element[C + 1])
    for i in range(C + 2, C + D + 2):
        ele = element[i]
        pushin = []
        pushin.append(ele[0])
        pushin.append(ele[1])
        oppose.append(pushin)

    N = int(element[C + D + 2])
    magic = []
    str0 = element[len(element) - 1]
    for i in range(0, N):
        if len(magic) == 0:
            magic.append(str0[i])
        else:
            end = len(magic) - 1
            com = 0
            opp = 0
            for j in range(0, C):
                if combine[j][0] == magic[end] and combine[j][1] == str0[i]:
                    com = 1
                    magic[end] = combine[j][2]
                    break
                if combine[j][1] == magic[end] and combine[j][0] == str0[i]:
                    com = 1
                    magic[end] = combine[j][2]
                    break
            if not com:
                for j in  range(0, D):
                    for item in magic:
                        if item == oppose[j][0] and str0[i] == oppose[j][1]:
                            magic = []
                            opp = 1
                            break
                        if item == oppose[j][1] and str0[i] == oppose[j][0]:
                            magic = []
                            opp = 1
                            break
                    if opp:
                        break
            
            if not com and not opp:
                magic.append(str0[i])
    
    sys.stdout.write("Case #")
    sys.stdout.write(str(iter + 1))
    sys.stdout.write(": [")
    #print "Case #%d: [" % (iter + 1),
    for i in range(0, len(magic) - 1):
        sys.stdout.write(magic[i])
        sys.stdout.write(", ")
    if (len(magic) > 0):
        sys.stdout.write(magic[len(magic) - 1])
    print "]"
