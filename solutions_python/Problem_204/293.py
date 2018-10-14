import math

if __name__ == "__main__":
    modelinput = 'B-small-attempt0.in'
    modeloutput = 'B-small-attempt0.out'

    inputlines = []
    with open(modelinput, 'r') as f:
        inputlines = f.readlines()

    numcases = int(inputlines.pop(0))

    with open(modeloutput,'w') as f:
        for casenum in range(numcases):
            ingredients = {}
            packages = {}

            temp = inputlines.pop(0)
            N = int(temp.split()[0])
            P = int(temp.split()[1])
            req = inputlines.pop(0)
            requirements = [int(r) for r in req.split()]
            for n in range(N):
                ingredients[n] = [int(x) for x in inputlines.pop(0).split()]
                packages[n] = []
                for i in ingredients[n]:
                    packages[n].append((math.ceil(i/(1.1*requirements[n])),math.floor(i/(0.9*requirements[n]))))
                    packages[n].sort(key=lambda x: x[0])
                    packages[n].sort(key=lambda x: x[1])
           # print(packages)
            total = 0
            while True:
                try:
                    lowers = []
                    uppers = []
                    packgroup = []
                    for n in range(N):
                        r = packages[n].pop(0)
                        packgroup.append(r)
                        lowers.append(r[0])
                        uppers.append(r[1])
                    while max(lowers) > min(uppers):
                        n = uppers.index(min(uppers))
                        r = packages[n].pop(0)
                        packgroup[n] = r
                        lowers[n] = r[0]
                        uppers[n] = r[1]
#                    print(packgroup)
                    total += 1
                except:
                    break

            strtowrite = 'Case #'+str(casenum+1)+": "+str(total)+"\n"
            f.write(strtowrite)
