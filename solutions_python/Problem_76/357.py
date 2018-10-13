def isNot0(q):
    for e in q:
        if e: return True
    return False

def sum(q):
    result = 0
    for e in q: result += e
    return result

def mod(q):
    result = list()
    for e in q: result.append(e%2)
    return result

def div(q):
    result = list()
    for e in q: result.append(e/2)
    return result

def removeMin(q):
    min = q[0]
    for e in q:
        if e < min: min = e
    q.remove(min)
    return q

def solve(q):
    q = q.split(" ")
    num = list()
    for n in q: num.append(int(n))

    test = num
    while isNot0(test):
        if sum(mod(test)) % 2 == 1: return "NO"
        test = div(test)

    result = sum(removeMin(num))

    return str(result)

fIn     = open('aInput', 'r')
fOut    = open('aOutput', 'r+')

fIn = fIn.readlines()
fIn = fIn[1:]
inp = list()
for i in range(len(fIn)/2):
    inp.append(fIn[2*i+1][:-1])

for i in range(len(inp)):
    e = inp[i]
    fOut.write("Case #" + str(i+1) + ": " + solve(e) + "\n")
