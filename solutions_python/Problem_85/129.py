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

def timeToN(n, C, a, s):
    time = s * (n / C)
    for i in range(n % C): time += a[i]
    return time * 2

def solveCase(line):
    data = explodeToInt(line, " ")
    L = data[0]
    t = data[1]
    N = data[2]
    C = data[3]
    a = data[4:]
    s = sum(a)
    for i in range(len(a), N):
        a.append(a[i % C])

    saved = []
    b1 = False
    for i in range(len(a)):
        if b1: saved.append(a[i])
        else:
            time = timeToN(i+1, C, a, s)
            if time >= t:
                b1 = True
                saved.append((time - t)/2)
            else:
                saved.append(0)

    saved.sort()
    ans = timeToN(N, C, a, s)
    if L > 0: ans -= sum(saved[-1*L:])

    return str(ans);

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

main("small")
