def tidy(n):
    strn = list(str(n))
    working = True
    while working:
        for i in range(len(strn) - 1):
            if (strn[i] > strn[i + 1]):
                # Decrease strn[i]
                strn[i] = str(int(strn[i]) - 1)
                for j in range(i+1, len(strn)):
                    strn[j] = '9'
                break
        else:
            working = False
    return int("".join(strn))


f = open("B-large.in", "r")

f.readline()  # discard number of test cases
fout = open("qualb.out", "w")

for num, line in enumerate(f):
    res = tidy(int(line.strip()))
    fout.write("Case #{}: {}\n".format(num+1, res))