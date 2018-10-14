def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def solveCase(line):
    data = explode(line, ' ')
    k1 = int(data[0]) + 1
    k2 = k1 + int(data[k1]) + 1
    comboPairs = {}
    for i in range(1, k1):
        a = data[i][0:1]
        b = data[i][1:2]
        c = data[i][2:3]
        comboPairs[a+b] = c
        comboPairs[b+a] = c
    opposedPairs = []
    for i in range(k1+1, k2):
        opposedPairs.append((data[i][0:1], data[i][1:2]))

    series = data[-1]
    result = []
    for i in range(len(series)):
        l = series[i:i+1]
        result.append(l)
        if len(result) == 1: continue
        if (result[-2] + l) in comboPairs:
            newL = comboPairs[result[-2] + l]
            for j in range(2): result.pop()
            result.append(newL)
            
        for j in range(len(result)):
            if (result[j], result[-1]) in opposedPairs or (result[-1], result[j]) in opposedPairs:
                result = []
                break

    out = "["
    for i in range(len(result)):
        if i > 0: out += ", "
        out += result[i]
    out += "]"

    return out

def process(data):
    out = ""
    for i in range(1, len(data)):
        if i > 1: out += '\n'
        out += "Case #" + str(i) + ": "
        out += solveCase(data[i])
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
