def flip(p,k,c):
    count = 0
    pl = list(p)
    maxcount = 10000
    while(True):
        if count == maxcount:
            break
        if "-" in pl:
            i = pl.index("-")
            if(i+k >= len(pl)):
                i = len(pl) - k
            for j in range(k):
                a = i+j
                s = "-"
                if (pl[a] == "-"):
                    s = "+"
                pl[a] = s
            count += 1
        else:
            break
    if count == maxcount:
        count = "IMPOSSIBLE"
    return ("Case #" + str(c) + ": " + str(count))

#fileName = "pan_cake_small_test.txt"
#fileName = "small.in"
fileName = "large.in"

fileobject = open(fileName, "r")

content = fileobject.read().strip()
lines = content.split("\n")
tc = int(lines[0])
lines = lines[1:]

outfile = list()

t = 1
for fline in lines:
    i = fline
    (p,k) = i.strip().split(" ")
    outfile.append(flip(p,int(k),t))
    t += 1
fileobject.close()

fileobject = open(fileName + ".out.txt", "w")
fileobject.write("\n".join(outfile))
fileobject.close()
