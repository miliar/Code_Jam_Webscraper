def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def getBot(seq, i):
    if i < 0: return ""
    return seq[2 * i + 1]

def getButton(seq, i):
    if i < 0: return 0
    return int(seq[2 * i + 2])

def solveCase(line):
    seq = explode(line, ' ')
    pos = {"O": 1, "B": 1}
    times = []
    for i in range(int(seq[0])):
        robot = getBot(seq, i)
        button = getButton(seq, i)
            
        otherRobotTime = 0
        j = i - 1
        while len(getBot(seq, j)) > 0 and getBot(seq, j) != robot:
            otherRobotTime += times[j]
            j -= 1

        thisRobotTime = abs(pos[robot] - button) + 1 - otherRobotTime
        if thisRobotTime < 1: thisRobotTime = 1
        times.append(thisRobotTime)
        pos[robot] = button

    totalTime = 0
    for i in times: totalTime += i
    return str(totalTime)

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
