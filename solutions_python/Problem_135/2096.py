infile = open("A-small-attempt1.in", "r")
outfile = open("magicout", "a")

lines = infile.readlines()
a = 0
g = -1

for line in lines:

    c = 0
    d = 0
    e = 0
    C = 0
    D = 0
    E = 0
    F = 0
    g += 1
    l = []
    M = []

    if a == 0:
        b = int(line[:-1])
        a += 1

    else:
        if (g - 1) % 5 == 0:
            Matrix = [[0 for x in range(5)] for x in range(5)]
            h = 0
            H = int(line[0])
            continue
        for j in range(len(line)):
            if line[j] == " " and c == 0 and d == 0 and e == 0:
                l.append(line[:j])
                c = j + 1
            elif line[j] == " " and d == 0 and e == 0:
                l.append(line[c:j])
                d = j + 1
            elif line[j] == " " and e == 0:
                l.append(line[d:j])
                e = j + 1
        l.append(line[e:-1])

        for i in range(4):
            Matrix[h][i] = l[i]

        if (g % 5) == 0 and (g % 10) != 0:
            L = Matrix[H-1]
        elif g % 10 == 0:
            m = Matrix[H-1]
            for i in range(4):
                for j in range(4):
                    if L[i] == m[j]:
                        M.append(L[i])

        h += 1

    if g % 10 == 0 and g != 0:
        p = int(g / 10)
        if len(M) == 1:
            outfile.write("Case #" + str(p) + ": " + M[0])
            outfile.write("\n")
        elif len(M) > 1:
            outfile.write("Case #" + str(p) + ": Bad magician!")
            outfile.write("\n")
        else:
            outfile.write("Case #" + str(p) + ": Volunteer cheated!")
            outfile.write("\n")

infile.close()
outfile.close()
