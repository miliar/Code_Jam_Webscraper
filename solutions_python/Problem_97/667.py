def getRecycleNumbers(n):
    l = len(repr(n))
    s2 = repr(n) + repr(n)
    result = []

    for i in range(l):
        recCandidate = s2[i:i+l]
        if recCandidate[0] != '0':
            j = int(recCandidate)
            if j not in result: result.append(j)

    return result

def solve(a, b):
    count = 0
    for n in range(a, b + 1):
        for m in getRecycleNumbers(n):
            if m > n and m <= b:
                count = count + 1
    return count

f = open('C-large.in', 'r')
f2 = open('C-large.out','w')
numOfCases = int(f.readline())

for case in range(numOfCases):
    values = f.readline().split(' ')
    result = "Case #" + repr(case+1) + ": " + repr(solve(int(values[0]), int(values[1]))) + "\n"
    f2.write(result)

f.close()
f2.close()
