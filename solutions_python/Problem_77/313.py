def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def isSorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]: return False
    return True

def findChain(aU, aS, dest, i):
    nextIndex = aS.index(aU[i])
    if dest == nextIndex: return [dest]
    return [nextIndex] + findChain(aU, aS, dest, nextIndex)

def rotateChain(aU, aS, dest, i):
    nextIndex = aS.index(aU[i])
    aU[i] = aS[i]
    if dest == nextIndex: return
    rotateChain(aU, aS, dest, nextIndex)

def solveCase(data):
    aU = explode(data, " ")
    for i in range(len(aU)):
        aU[i] = int(aU[i])
    aS = []
    for i in aU: aS.append(i)
    aS.sort()
    i = -1
    n = len(aS)
    count = 0

    while i < n-1:
        i += 1
        if aU[i] == aS[i]: continue
        chain = findChain(aU, aS, i, i)
        rotateChain(aU, aS, i, i)
        if len(chain) > 1: count += len(chain)
    return "%0.6f" % count

def process(data):
    out = ""
    caseNum = 1
    for i in range(2, len(data), 2):
        if caseNum > 1: out += '\n'
        out += "Case #" + str(caseNum) + ": "
        out += solveCase(data[i])
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

main("small")
