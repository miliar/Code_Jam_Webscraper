f = open("A-large.in", "r").read()


lines = f.split("\n")
cases = int(lines[0])


for case in range(1, cases+1):
    line = lines[case]
    columns = line.split(" ")
    str = columns[0]
    k = int(columns[1])

    s = list(str)

    count = 0

    for i in range(0, len(s) - (k - 1)):
        if s[i] == "-":
            count += 1
            for j in range(0, k):
                s[i+j] = "+" if s[i+j] == "-" else "-"
        else:
            pass


    if "-" in s:
        print("Case #{0}: IMPOSSIBLE".format(case))
    else:
        print("Case #{0}: {1}".format(case, count))