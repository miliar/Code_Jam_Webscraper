def intersect(a, b):
     return list(set(a) & set(b))

def readLine(content):
    L = int(content.pop(0)) # get line num
    line = content.pop(L-1);  # get target line
    for x in range(3):
        content.pop(0);     # remove 3 other lines
    return map(int, line.split())

def findResult(line1, line2):
    intr = intersect(line1, line2)
    inum = len(intr);
    if (inum == 1):
        return intr[0];
    elif (inum == 0):
        return "Volunteer cheated!";
    else:
        return "Bad magician!";


fname = "A-small-attempt0.in"
with open(fname) as f:
    content = f.readlines();

    T = int(content.pop(0))

    with open("magic.out.txt", "w+") as fout:
        for i in range(T):
            line1 = readLine(content)
            line2 = readLine(content)
            res = "Case #%d: %s" % (i+1, findResult(line1, line2))
            print res
            fout.write(res)
            fout.write("\n")

