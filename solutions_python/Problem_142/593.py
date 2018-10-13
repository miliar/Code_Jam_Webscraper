fin = open("input.txt", 'r')
fout = open("output.txt", 'w')
tests = int(fin.readline())
for t in range(1, tests + 1):
    N = int(fin.readline())
    s1 = fin.readline().rstrip()
    s2 = fin.readline().rstrip()
    c = 0
    can = 1
    while len(s1) != 0 and len(s2) != 0:
        i = 0
        el1 = s1[0]
        el2 = s2[0]
        if el1 != el2:
            can = 0
            break
        while i < len(s1) and s1[i] == el1:
            i += 1
        j = 0
        while j < len(s2) and s2[j] == el2:
            j += 1
        s1 = s1[i:]
        s2 = s2[j:]
        c += abs(i - j)
    print(s1, s2)
    if len(s1) != 0 or len(s2) != 0:
        can = 0
    if can:
        fout.write("Case #" + str(t) + ": " + str(c) + "\n")
    else:
        fout.write("Case #" + str(t) + ": Fegla Won\n")

fin.close()
fout.close()
