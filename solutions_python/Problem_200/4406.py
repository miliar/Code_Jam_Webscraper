def isTidy(num):
    num = str(num)
    tidy = True
    for x in range(0, len(num)-1):
        if int(num[x]) > int(num[x+1]):
            return False
    return True

def findTidy(num):
    for x in range(num, 0, -1):
        if isTidy(x):
            return x

caseNum = int(input())
for x in range(1, caseNum+1):
    caseVal = int(input())
    print("Case #" + str(x) + ": " + str(findTidy(caseVal)))
