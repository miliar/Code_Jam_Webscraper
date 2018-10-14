f = open("B-small-attempt0.in","r")
g = open("output.txt","w")
info = f.read().split("\n")
print info
n = int(info.pop(0))
print n


for i in range(n):
    nondec = []
    num = int(info[i])
    for a in range(num+1):
        if a==0:
            continue
        else:
            numstr = str(a)
            if len(numstr)==1:
                nondec.append(numstr)
            elif len(numstr)==2:
                if int(numstr[0]) <= int(numstr[1]):
                    nondec.append(numstr)
            else:
                if int(numstr[0]) <= int(numstr[1]) <= int(numstr[2]):
                    nondec.append(numstr)
    g.write("Case #" + str(i+1) + ": " + str(int(nondec[len(nondec)-1])) + "\n")
