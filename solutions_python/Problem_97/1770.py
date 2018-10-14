f = open('small.in', 'r')
outputf = open('small.out', 'w')
i =  int(f.readline())
def isRecycled(i, j):
    if(j in (i + i)):
        return True
    return False
for m in range(0, i):
    vals = [x for x in f.readline().rstrip().split(' ')]
    a = vals[0]
    b = vals[1]
    sum = 0
    for x in range(int(a), int(b)):
        for y in range(x + 1, int(b) + 1):
            if isRecycled(str(x), str(y)):
                sum = sum + 1
    outputf.write("Case #" + str(m + 1) + ': ' + str(sum) + '\n')
