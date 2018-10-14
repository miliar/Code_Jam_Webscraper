import re

def alien1(line):
    n, src, trj = line.strip("\n").split(" ")
    x, res = 0, ""
    for digit in str(n):
        x = x * len(src) + src.index(digit)    
    while x > 0:
        res = trj[x%len(trj)] + res
        x = int(x/len(trj))
    return res

def alien2(file):
    lines = map(lambda x: x[:-1], open(file, 'r').readlines())
    l, d, n = lines[0].strip("\n").split(" ")
    words = lines[1:int(d)+1]
    patterns = map(lambda x: x.replace("(","[").replace(")","]"), lines[int(d)+1:])
    cases = list()
    for pattern in patterns:
        count = 0
        regex = re.compile(pattern)
        for word in words:
            if regex.match(word): count += 1
        cases.append(str(count))
    return cases
    

##results = map(alien, open("in.in", 'r').readlines()[1:])
results = alien2("in.in")
for i in range(0, len(results)):
    print "Case #" + str(i+1) + ": " + results[i]