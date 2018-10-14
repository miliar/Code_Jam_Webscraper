infile = open("B-large.in")
outfile = open("B-large.out", "w")
T = int(infile.readline())
for testcaseN in range(T):
    N = infile.readline().strip()
    i = len(N) - 1
    removed = [int(N[i])]
    maxRemoved = removed[0]
    result = ""
    while True:
        i -= 1
        if i < 0:
            removed.sort()
            if removed[0] == 0:
                j = 1
                while removed[j] == 0:
                    j += 1
                removed[0] = removed[j]
                removed[j] = 0
            result = str(removed[0]) + "0" + "".join([str(el) for el in removed[1:]])
            break
        d = int(N[i])
        if d < maxRemoved:
            minGreater = -1
            for el in removed:
                if el > d and (minGreater == -1 or el < minGreater):
                        minGreater = el
            removed.remove(minGreater)
            removed.append(d)
            removed.sort()
            result = N[0:i] + str(minGreater) + "".join([str(el) for el in removed])
            break
        else:
            removed.append(d)
            if d > maxRemoved:
                maxRemoved = d
    outfile.write("Case #" + str(testcaseN + 1) + ": " + result + "\n")