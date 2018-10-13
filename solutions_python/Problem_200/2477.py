#!/usr/bin/python
def solve (numStr):
    numLen = len(numStr)
    ans = ""
    pos = numLen
    for i in range(numLen-1):
        if numStr[i] > numStr[i+1]:
            pos = i + 1
            break
    if pos ==  numLen:
        return numStr  #no change
    for i in range (pos, -1, -1):
        if numStr[i] > '1':
            return solve(numStr[:i] + chr( ord(numStr[i]) - 1 ) + '9'*(numLen-i-1))
    return '9'*(numLen-1)

testCase = int(input())
for m in range (1, testCase+1):
    intNum = str( input())
    ans = solve(intNum)
    print("Case #{}: {}".format(m, ans) )#->



