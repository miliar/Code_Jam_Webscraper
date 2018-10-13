def flip(aList, start, finish):
    for i in range(start, finish):
        if aList[i] == '-':
            aList[i] = '+'
        else:
            aList[i] = '-'

def calculate(S, K):
    aList = list(S)
    result = "IMPOSSIBLE"
    count = 0
    i = 0
    while i+K <= len(aList):
        if aList[i] == '+':
            i += 1
        else:
            flip(aList, i, i+K)
            count += 1
            i += 1
    if ''.join(aList[i:]) == ('+' * len(aList[i:])):
        result = count
    return str(result)

#file read operation
t = int(raw_input()) # number of S

for i in xrange(1, t + 1):
    line = raw_input().split(" ")
    S, K = str(line[0].strip()), int(line[1].strip())
    print "Case #{}: {}".format(i, calculate(S, K))
