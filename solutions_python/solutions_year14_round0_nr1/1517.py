infile = open("input.txt", "r")
outfile = open("output.txt", "w")

t = int(infile.readline())
for i in range(t):
    pos = int(infile.readline())
    s1 = set()
    for j in range(4):
        string = list(map(int, infile.readline().split()))
        if pos - 1 == j:
            for x in string:
                s1.add(x)
    pos = int(infile.readline())
    s2 = set()
    for j in range(4):
        string = list(map(int, infile.readline().split()))
        if pos - 1 == j:
            for x in string:
                s2.add(x)
    sres = s1 & s2
    print("Case #", i + 1, ": ", sep = "", end = "", file = outfile)
    if len(sres) == 1:
        print(*sres, file = outfile)
    elif len(sres) == 0:
        print("Volunteer cheated!", file = outfile)
    else:
        print("Bad magician!", file = outfile)