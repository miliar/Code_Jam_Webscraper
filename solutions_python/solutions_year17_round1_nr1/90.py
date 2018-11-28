import sys

INPUT_NAME = sys.argv[1]
OUTPUT_NAME = INPUT_NAME.split(".")[0] + ".out"

f = open(INPUT_NAME,'r')
out = open(OUTPUT_NAME,'w')

num_cases = int(f.readline().strip())

for test in range(num_cases):
    r,c = tuple(map(int,f.readline().strip().split(" ")))
    L = [list(f.readline().strip()) for i in range(r)]
    for i in range(len(L)):
        if L[i].count("?") < c:
            x = "-"
            for char in L[i]:
                if char != "?":
                    x = char
                    break
            j = 0
            while j<c:
                if L[i][j] == "?":
                    L[i][j] = x
                elif L[i][j] != x:
                    x = L[i][j]
                j += 1
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == "?" and i > 0:
                L[i][j] = L[i-1][j]
    for i in reversed(range(len(L))):
        for j in range(len(L[i])):
            if L[i][j] == "?":
                L[i][j] = L[i+1][j]

    out.write("Case #%d:\n" % (test+1))
    for i in range(r):
        out.write("".join(L[i]) + "\n")
