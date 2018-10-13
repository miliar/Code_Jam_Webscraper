f = open("QB.in", "r")
out = open("QB.out", "w")
n = int(f.readline())
for t in range(n):
    m = f.readline().split()
    m = [int(x) for x in m[0]]
    l = [-1 for i in range(len(m))]
    l[0] = m[0]
    for i in range(1, len(m)):
        if l[i - 1] <= m[i]:
            l[i] = m[i]
        else:
            ii = i - 1
            l[ii] -= 1
            while ii > 0 and l[ii] < l[ii - 1]:
                l[ii - 1] -= 1
                ii -= 1
            for j in range(ii + 1, len(m)):
                l[j] = 9
            break
    out.write("Case #" + str(t + 1) + ": ")
    b = True
    for ll in l:
        if ll != 0 or b == False:
            b = True
            out.write(str(ll))
    out.write("\n")