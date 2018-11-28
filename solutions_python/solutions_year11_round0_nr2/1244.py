t, T = 0, int(raw_input())
while t != T:
    t += 1
    line = raw_input().split()

    C = dict()
    for i in range(int(line.pop(0))):
        s = line.pop(0)
        C[s[0]] = dict()
        C[s[1]] = dict()
        C[s[0]][s[1]] = s[2]
        C[s[1]][s[0]] = s[2]

    O = dict()
    for i in range(int(line.pop(0))):
        s = line.pop(0)
        O[s[0]] = s[1]
        O[s[1]] = s[0]

    N = int(line.pop(0))
    out = []
    for c in line.pop(0):
        if out:
            if c in C and out[-1] in C[c]:
                out[-1] = C[c][out[-1]]
            elif c in O and O[c] in out:
                out = []
            else:
                out.append(c)
        else:
            out.append(c)

    print "Case #%d:"%t, str(out).replace("'","")
