def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

nums = []
def findRecycledNumbers():
    for i in range(1, 1000):
        for j in range(i+1, 1001):
            if recycled(i, j):
                nums.append([i, j])

def recycled(m, n):
    M = str(m)
    N = str(n)
    for i in range(len(M)):
        M1 = M[i:] + M[:i]
        if M1 == N: return True
    return False

def solveCase(line):
    data = explode(line, ' ')
    A = int(data[0])
    B = int(data[1])
    n = 0
    for i in nums:
        if i[0] >= A and i[1] <= B: n+=1
    return n

def process(data):
    out = ""
    for i in range(1, len(data)):
        if i > 1: out += '\n'
        out += "Case #" + str(i) + ": "
        out += str(solveCase(data[i]))
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
