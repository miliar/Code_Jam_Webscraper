def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def explodeToInt(s, c):
    a = explode(s, c)
    for i in range(len(a)): a[i] = int(a[i])
    return a

def fourBlue(rows, i, j):
    return rows[i][j] == "#" and rows[i+1][j] == "#" and rows[i][j+1] == "#" and rows[i+1][j+1] == "#"

def makeRed(rows, i, j):
    r1 = copy(rows[i])
    r2 = copy(rows[i+1])
    r1[j] = "/"
    r2[j] = '\\'
    r1[j+1] = '\\'
    r2[j+1] = "/"
    rows[i] = listConcat(r1)
    rows[i+1] = listConcat(r2)

def listConcat(a):
    s = ""
    for i in a:
        s += str(i)
    return s

def copy(a):
    b = []
    for i in a: b.append(i)
    return b

def solve(candidates, rows, s, memo):
    if s in memo: return memo[s]
    if not "#" in s: return rows
    c = copy(candidates)
    ans = "Impossible"
    for i in c:
        r = copy(rows)
        if fourBlue(r, i[0], i[1]):
            makeRed(r, i[0], i[1])
            d = copy(c)
            d.remove(i)
            tempAns = solve(d, r, listConcat(r), memo)
            if tempAns != "Impossible":
                ans = tempAns
                break
    memo[s] = ans
    return ans            

def solveCase(rc, rows):
    R = rc[0]
    C = rc[1]
    candidates = []
    for i in range(R-1):
        for j in range(C-1):
            if fourBlue(rows, i, j):
                candidates.append((i,j))
    memo = {}
    ans = solve(candidates, rows, listConcat(rows), memo)
    out = ""
    if ans == "Impossible": out = "\nImpossible"
    else:
        for i in ans:
            out += '\n' + i
    return out

def process(data):
    for i in range(len(data)): data[i] = explode(data[i], '\n')[0]
    out = ""
    i = 1
    for case in range(int(data[0])):
        if case > 0: out += '\n'
        out += "Case #" + str(case+1) + ": "
        rc = explodeToInt(data[i], " ")
        rows = []
        for j in range(rc[0]): rows.append(data[i+1+j])
        i += (1+int(rc[0]))
        out += solveCase(rc, rows)
    return out

def main(fn):
    iFile = open(fn + ".in", "r")
    oFile = open(fn + ".out", "w")
    print("Files opened.")

    data = []
    while True:
        line = iFile.readline()
        if not line: break
        data.append(line)

    out = process(data)
    print("Calculations complete. Outputting to file.")
    oFile.writelines(out)
    print("Output complete.")
    iFile.close()
    oFile.close()
    print("Files closed.")

main("small")
