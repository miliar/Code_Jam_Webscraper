__author__ = 'yurychebiryak'

import itertools

def compress(s):
    res = ''.join(c for c, _ in itertools.groupby(s))
    return res

def mycount(s):
    res = []
    compressed = compress(s)
    i = 0
    count = 0
    for j in range(len(s)):
        if s[j] == compressed[i]:
            count += 1
        else:
            res.append(count)
            count = 1
            i+=1
    res.append(count)
    return res

def isFeasible(strings):
    compressed = set()
    for s in strings:
        compressed.add(compress(s))
    if len(compressed) == 1:
        return True
    return False

def transform(a,b):
    i =0
    j =0
    res = 0
    while not( (i == len(a) -1) and (j == len(b) - 1)):
        if a[i] == b[j]:
            if (i < len(a) -1) and (j < len(b) - 1):
                i+=1
                j+=1
                continue
            if (i == len(a) -1):
                res += 1
                j+=1
                continue
            if (j == len(b) - 1):
                res += 1
                i += 1
                continue
        # a[i] != b[j]
        if (i > 0) and (a[i-1] == b[j]):
            res +=1
            j+=1
            continue
        if (j > 0) and (b[j-1] == a[i]):
            res+=1
            i+=1
            continue
        print("Error in i = %d, j=%d" % (i,j))
    return res

def findMaxCount(strings):
    res = mycount(compress(strings[0]))
    for s in strings:
        c = mycount(s)
        for i in range(len(res)):
            if res[i] < c[i]:
                res[i] = c[i]
    return res

def genTrans(strings):
    res = []
    counts = findMaxCount(strings)
    compressed = mycount(compress(strings[0]))
    current = compressed
    res.append(list(current))
    while current != counts:
        for i in range(len(current)):
            if current[i] < counts[i]:
                current[i] = current[i] + 1
                for j in range(i):
                    current[j] = 1
                break
        #generate string
        res.append(list(current))
    return res

def genTransStrings(strings):
    compressed = compress(strings[0])
    counts = genTrans(strings)
    res = []
    for c in counts:
        s = ""
        for i in range(len(c)):
            for k in range(c[i]):
                s += compressed[i]
        res.append(s)
    return res

def solve(strings):
    maxTurns = 10000000
    solutions = strings#genTransStrings(strings)
    for sol in solutions:
        turns = 0
        for str in strings:
            turns += transform(str, sol)
        if turns < maxTurns:
            maxTurns = turns
    return maxTurns

def run(input, output):
    file = open(input, 'r')
    out = open(output, 'w')
    lines = file.readlines()
    current = 0
    for i in range(int(lines[0].strip())):
        current +=1
        n = int(lines[current].strip())
        strings = []
        for j in range(n):
            current += 1
            strings.append(lines[current].strip())

        out.write("Case #%d: " % (i+1) )
        print("Case #%d: " % (i+1) )
        if isFeasible(strings):
            ways = solve(strings)
            out.write("%d\n" % ways)
            print("%d\n" % ways)
        else:
            out.write("Fegla Won\n")
            print("Fegla Won\n")

run("example.txt", "exampleOut.txt")
run("small.txt", "smallOut.txt")
#run("big.txt", "bigOut.txt")
#print(genTrans(["abbbcc"]))
#genTransStrings(["abbbcc"])
#print(genTransStrings(["mmaw", "maw"]))