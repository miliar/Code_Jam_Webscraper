def explodeInt(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(int(s[p:i]))
            p = i + 1
    return t

def solveCase(lines):
    rows = []
    for i in lines: rows.append(explodeInt(i, ' '))
    rowMax = []
    colMax = []
    for i in rows:
        rowMax.append(i[0])
        for j in i:
            if j > rowMax[-1]: rowMax[-1] = j
    for j in range(len(rows[0])):
        colMax.append(rows[0][j])
        for i in range(len(rows)):
            if rows[i][j] > colMax[j]: colMax[j] = rows[i][j]
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] != min(rowMax[i], colMax[j]): return "NO"
    return "YES";

def process(data):
    out = ""
    caseNum = 1
    T = int(data[0])
    pos = 1
    for i in range(T):
        if caseNum > 1: out += '\n'
        n = int(explodeInt(data[pos], ' ')[0])
        lines = []
        for j in range(n): lines.append(data[pos+j+1])
        pos += (n + 1)
        out += "Case #" + str(caseNum) + ": "
        out += solveCase(lines)
        print out
        caseNum += 1
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

main("large")
