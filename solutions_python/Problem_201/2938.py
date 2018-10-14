def calL(i, L):
    m = 0
    while (type(L[i - 1]) == type(L)):
        m += 1
        i -= 1
    return (m)


def calR(i, L):
    m = 0
    while (type(L[i + 1]) == type(L)):
        m += 1
        i += 1
    return (m)


def calNum(i, L):
    val = 0
    Ls = calL(i, L)
    Rs = calR(i, L)
    return ([val, Ls, Rs])


def minLR(i, L):
    if (L[i][1] > L[i][2]):
        return (L[i][2])
    elif (L[i][1] < L[i][2]):
        return (L[i][1])
    else:
        return (L[i][2])


def maxLR(i, L):
    if (L[i][1] < L[i][2]):
        return (L[i][2])
    elif (L[i][1] > L[i][2]):
        return (L[i][1])
    else:
        return (L[i][1])


def judgeMinMax(L):
    JXD = []
    res = []
    da = -1
    for i in range(1, L.__len__() - 1):
        if (type(L[i]) == type(L)):
            JXD.append([i, minLR(i, L)])
    for j in JXD:
        if (j[1] > da):
            da = j[1]
    for k in JXD:
        if (k[1] == da):
            res.append(k[0])
    return (res)


def judgeMaxMax(J, L):
    JDD = []
    res = []
    da = -1
    for i in J:
        JDD.append([i, maxLR(i, L)])
    for j in JDD:
        if (j[1] > da):
            da = j[1]
    for k in JDD:
        if (k[1] == da):
            res.append(k[0])
    return (res)


def judge(L):
    J = judgeMinMax(L)
    if (J.__len__() > 1):
        JMM = judgeMaxMax(J, L)
        pos = JMM[0]
        return (pos)
    else:
        pos = J[0]
        return (pos)


def start(a, b):
    a = int(a)
    b = int(b)
    # create list
    L = [1]
    for i in range(0, a):
        L.append([0, i, a - i - 1])
    L.append(1)

    while (b > 1):
        L[judge(L)] = 1;
        for i in range(1, L.__len__() - 1):
            if (type(L[i]) == type(L)):
                L[i] = calNum(i, L)
        if (b == 2):
            print(L)
        b -= 1

    while(b==1):
        Ls = L[judge(L)][1]
        Rs = L[judge(L)][2]
        if (Ls >= Rs):
            max = Ls
            min = Rs
        else:
            max = Rs
            min = Ls
        break

    return max, min


l = []
out = open('C-small-1-attempt2.out', 'w')
for line in open('C-small-1-attempt2.in', 'r'):
    if (line.__contains__(" ")):
        l.append(line.split())
    else:
        times = int(line.strip())
# print(l)
ot=[]
# times = 1
for i in range(0, times):
    print(i+1)
    # print(i, l[i][0], l[i][1])
    max, min = start(l[i][0], l[i][1])
    # max,min = start(500,2)
    # print(max, min)
    ot.append([max, min])

for i in range(0, times):
    out.write("Case #{}: {} {}\n".format(i + 1, ot[i][0], ot[i][1]))
out.close()
