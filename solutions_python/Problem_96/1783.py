def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def possibleN(p, t):
    return t >= 3*p - 2

def possibleS(p, t):
    for i in range(p, 11):
        if 3*i-4 <= t and t <= 3*i-2 and i-2 >= 0: return True
    return False

def solveCase(line):
    data = explode(line, ' ')
    S = int(data[1])
    N = int(data[0]) - S
    p = int(data[2])
    data = data[3:]
    x = [0, 0, 0, 0]
    for i in data:
        pN = possibleN(p, int(i))
        pS = possibleS(p, int(i))
        if pS and not pN: x[0]+=1
        if pN and not pS: x[1]+=1
        if pS and pN: x[2]+=1
        if not pS and not pN: x[3]+=1
    M = 0
    if x[0] >= S: M = x[1]+x[2]+S
    else:
        M+=(x[0]+x[2])
        if x[1] <= N: M+=x[1]
        else: M+=N
    return M;

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
