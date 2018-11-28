fin = open("input.txt", 'r')
fout = open("output.txt", 'w')
tests = int(fin.readline())
for t in range(1, tests + 1):
    N = int(fin.readline())
    s1 = fin.readline().rstrip()
    s2 = fin.readline().rstrip()
    a1 = []
    a2 = []
    c = 0
    for i in range(len(s1)):
        el = s1[i]
        if el not in a1:
            a1.append(el)
    for i in range(len(s2)):
        el = s2[i]
        if el not in a2:
            a2.append(el)
    print(a1, a2)
    can = 1
    if len(a1) != len(a2):
        can = 0
    else:
        for i in range(len(a1)):
            if a1[i] != a2[i]:
                can = 0
                break
    if can == 0:
        fout.write("Case #" + str(t) + ": Fegla Won\n")
    while len(s1) != 0 and len(s2) != 0:
        el1 = s1[0]
        el2 = s2[0]
        i = 0
        h1 = 0
        h2 = 0
        while i < len(s1) and s1[i] == el1:
            i += 1
        j = 0
        while j < len(s2) and s2[j] == el2:
            j += 1
        c += abs(i - j)
        s1 = s1[i:]
        s2 = s2[j:]
    if can == 1:
        fout.write("Case #" + str(t) + ": " + str(c) + '\n')



fin.close()
fout.close()
