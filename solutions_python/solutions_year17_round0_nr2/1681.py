def checkTidy(n):
    l = len(n)
    if l == 1:
        return True
    l -= 1
    while l > 0:
        if n[l] < n[l-1]:
            return False
        l -= 1
    return True

def lastTidy(n):
    l = len(n) - 1
    while not checkTidy(n):
        n[l] = 9
        n[l-1] -= 1
        l -= 1

def arrayToStr(n):
    s = ""
    if n[0] == 0:
        for i in range(1, len(n)):
            s += str(n[i])
    else:
        for i in range(len(n)):
            s += str(n[i])
    return s

fileName = "B-large.in"
f = open(fileName, 'r')

outputName = "B-large-out.txt"
output = open(outputName, 'w')

line = f.readline()
T = int(line)

for t in range(T):
    line = f.readline().strip()
    l = len(line)
    number = []
    for i in range(l):
        number.append(int(line[i]))
        
    res = ""
    if checkTidy(number):
        res = line
    else:
        lastTidy(number)
        res = arrayToStr(number)
    
    print("Case #{}: {}".format(t+1, res))
    output.write("Case #{}: {}".format(t+1, res))
    output.write("\n")

output.close()