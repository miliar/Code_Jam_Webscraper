from math import log

def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def toBinary(n):
    r = []
    if n == 0: return [0]
    highest = int(log(n, 2))
    for i in range(highest, -1, -1):
        r.append(n / pow(2, i))
        n -= pow(2, i) * r[-1]
    return r

def toDecimal(a):
    n = 0
    for i in range(len(a)):
        n += a[i] * pow(2, len(a) - i - 1)
    return n

def addWrong(n1, n2):
    a = toBinary(max(n1, n2))
    b = toBinary(min(n1, n2))
    d = len(a) - len(b)
    for i in range(len(b)):
        a[i + d] = (a[i + d] + b[i]) % 2
    return toDecimal(a)

def maximize(candy, totalValue, patricksCountHisPile, patricksCountSeansPile, seansCount, index, memo):    
    if index == len(candy):
        if patricksCountHisPile == patricksCountSeansPile and seansCount < totalValue: return seansCount
        return "NO"
    
    key = (patricksCountHisPile, patricksCountSeansPile, seansCount, index)
    if key in memo: return memo[key]
    
    giveIt = maximize(candy, totalValue, addWrong(patricksCountHisPile, candy[index]), patricksCountSeansPile, seansCount, index + 1, memo)
    keepIt = maximize(candy, totalValue, patricksCountHisPile, addWrong(patricksCountSeansPile, candy[index]), seansCount + candy[index], index + 1, memo)
    if giveIt == "NO" and keepIt == "NO": ans = "NO"
    elif giveIt == "NO": ans = keepIt
    elif keepIt == "NO": ans = giveIt
    elif giveIt > keepIt: ans = giveIt
    else: ans = keepIt
    memo[key] = ans
    return ans

def solveCase(line):
    candy = explode(line, ' ')
    memo = {}
    for i in range(len(candy)): candy[i] = int(candy[i])
    return str(maximize(candy, sum(candy), 0, 0, 0, 0, memo))

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
