fin = open("a.in")
fout = open("a.out", "w")

nt = int(fin.readline())

def toint(sign):
    if sign == '-':
        return 0
    return 1

for tn in xrange(nt):
    fout.write("Case #" + str(tn + 1) + ": ")

    s = fin.readline().strip()
    n = int(s.split()[1])
    s = s.split()[0]
    a = [toint(c) for c in s]
    ind = 0
    res = 0
    while ind < len(a):
        if a[ind] == 0:
            if ind + n  - 1 < len(a):
                res += 1
                for j in range(ind, ind + n):
                    a[j] = 1 - a[j]
            else:
                res = -1
                break
        ind += 1

    if res >= 0:
        fout.write(str(res))
        fout.write('\n')
    else:
        fout.write("IMPOSSIBLE\n")
