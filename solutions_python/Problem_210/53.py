import pprint





TEST = "B-large"
f1 = open(TEST+".in")
f2 = open(TEST+".out", "w")

T_max = int(f1.readline())
for T in range(T_max):
    f2.write("Case #%s: " % (T+1))
    print("Case #%s " % (T+1))

    Ac, Aj = map(int, f1.readline().split())

    C = []
    usedC = 0
    for i in range(Ac):
        Ci,Di = map(int, f1.readline().split())
        C.append((Ci,Di))
        usedC += Di-Ci
    J = []
    usedJ = 0
    for i in range(Aj):
        Ji,Ki = map(int, f1.readline().split())
        J.append((Ji,Ki))
        usedJ += Ki-Ji

    All = []
    for x in C:
        All.append((x[0],x[1],0))
    for x in J:
        All.append((x[0],x[1],1))
    All.sort()
    #print(All)

    Cint = []
    Jint = []
    CJint = []
    for i in range(len(All)):
        if(All[i-1][2] == 0 and All[i][2] == 0):
            x = All[i][0] - All[i-1][1]
            if(x < 0):
                x += 24*60
            Cint.append(x)
        elif (All[i - 1][2] == 1 and All[i][2] == 1):
            x = All[i][0] - All[i-1][1]
            if (x < 0):
                x += 24 * 60
            Jint.append(x)
        else:
            x = All[i][0] - All[i-1][1]
            if (x < 0):
                x += 24 * 60
            CJint.append(x)

    Cint.sort()
    Jint.sort()
    CJint.sort()


    for i in range(len(Cint)):
        if(usedC == 720):
            break
        can_use = min(720-usedC, Cint[i])
        Cint[i] -= can_use
        usedC += can_use

    for i in range(len(Jint)):
        if(usedJ == 720):
            break
        can_use = min(720-usedJ, Jint[i])
        Jint[i] -= can_use
        usedJ += can_use

    # print(usedC, usedJ)
    # print(Cint, Jint, CJint)

    ans = 0
    for x in Cint:
        if(x != 0):
            ans += 2
    for x in Jint:
        if(x != 0):
            ans += 2
    ans += len(CJint)
    f2.write("%s\n" % ans)