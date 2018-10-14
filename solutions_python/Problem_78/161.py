from math import ceil

def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def gcd(a, b):
    if b == 0: return a
    return int(gcd(b, a % b))

def lcm(a, b):
    return a * b / gcd(a, b)

def solveCase(line, lineNum):
    data = explode(line, " ")
    N = int(data[0])
    Pd = int(data[1])
    Pg = int(data[2])

    if (Pg == 100 and Pd < 100) or (Pg == 0 and Pd > 0): return "Broken"
    
    dWon = Pd / gcd(Pd, 100)
    if Pd == 0: dPlayed = 1
    else: dPlayed = 100 / gcd(Pd, 100)
    gWon = Pg / gcd(Pg, 100)
    if Pg == 0: gPlayed = 1
    else: gPlayed = 100 / gcd(Pg, 100)
    
    if dWon > gWon:
        f = int(ceil(dWon / gWon))
        gWon *= f
        gPlayed *= f
    if dPlayed > gPlayed:
        f = int(ceil(dPlayed / gPlayed))
        gWon *= f
        gPlayed *= f
    #print str(lineNum) + ": ", dWon, dPlayed, gWon, gPlayed, N, dPlayed <= N
    if dPlayed <= N: return "Possible"
    return "Broken";

def process(data):
    out = ""
    for i in range(1, len(data)):
        if i > 1: out += '\n'
        out += "Case #" + str(i) + ": "
        out += solveCase(data[i], i)
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
