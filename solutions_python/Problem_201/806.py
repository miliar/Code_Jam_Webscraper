__author__ = 'jlinenthal'

import math
#filename = "C-small-2-attempt0"
#filename = "CTest"
filename = "C-large"

infile = filename+ ".in"
outfile = filename+ ".out"

f_in = open(infile, 'r')
f_out = open(outfile, 'w')

t = int(f_in.readline().strip())

for aaa in range(0,t):
    line = f_in.readline().strip()
    nOrig = list(map(lambda x: 0 if x == '-' else 1, line.split(" ")[0]))
    n = int(line.split(" ")[0])
    k = int(line.split(" ")[1])

    depth = math.ceil(math.log(n,2))
    numSeen = 0
    structure = {n: 1}
    good = False

    if n == k:
        print("Case #{0}: {1} {2}\n".format(aaa+1, 0, 0))
        f_out.write("Case #{0}: {1} {2}\n".format(aaa+1, 0, 0))
        continue
    for i in range(0,depth):
        print(structure, numSeen, i , depth)
        nextStructure = {}
        for n in sorted(structure.keys(), reverse=True):
            if n == 0:
                continue
            count = structure[n]

            if n == 2:
                key = 1
                if key not in nextStructure:
                    nextStructure[key] = 0
                nextStructure[key] += count
            elif (n-1) % 2 == 0:
                key = (n - 1)//2
                if key not in nextStructure:
                    nextStructure[key] = 0
                nextStructure[(n - 1)//2] += 2*count
            else:
                key1 = (n - 1) // 2
                key2 = (n - 1) // 2 + 1
                if key1 not in nextStructure:
                    nextStructure[key1] = 0
                if key2 not in nextStructure:
                    nextStructure[key2] = 0
                nextStructure[key1] += count
                nextStructure[key2] += count
            numSeen += count
            #print("after assign", k, numSeen, nextStructure)
            if(k <= numSeen):
                # n is the number that was chosen
                #f_out.write("Case #{0}: {1}\n".format(aaa+1, res))
                print("hi")
                if n % 2 == 0:
                    maxVal = n // 2
                    minVal = n // 2 - 1
                else:
                    maxVal = (n-1) // 2
                    minVal = maxVal
                f_out.write("Case #{0}: {1} {2}\n".format(aaa+1, maxVal, minVal))
                print("Case #{0}: {1} {2}\n".format(aaa+1, maxVal, minVal))
                good = True
                break
        if good:
            break
        structure = nextStructure





#line = f_in.readline().strip()
#k = int(line.split()[0])
#c = int(line.split()[1])

