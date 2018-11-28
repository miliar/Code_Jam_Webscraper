case = 1

with open("output.txt","w") as o:
    with open("A-large.in","r") as i:
        for line in i:
            count = 0
            s = line.split()
            if len(s) > 1:
                localCount = 0
                for i in range(len(s[1])):
                    val = int(s[1][i])
                    while i > localCount:
                        localCount += 1
                        count += 1
                    localCount += val
                print("Case #"+str(case)+": "+str(count),file=o)
                case += 1