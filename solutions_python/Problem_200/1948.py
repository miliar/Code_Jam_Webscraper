#file read operation
t = int(raw_input()) # number of Input

def solve(number):
    aList = list(number)
    i = 0
    while i < len(aList) - 1:
        if int(aList[i]) <= int(aList[i+1]):
            i += 1
        else:
            if aList[i+1] == '0':
                aList[i] = str(int(aList[i]) -1)
                aList[i+1:] = '9' * len(aList[i+1:])
            else:
                aList[i+1] = str(int(aList[i+1]) -1)
            if i != 0:
                i -= 1
    index = 0
    while index < len(aList):
        if aList[index] == '0':
            index += 1
        else:
            break
    if len(aList[index:]) == 0:
        return '0'
    return ''.join(aList[index:])

for i in xrange(1, t + 1):
    number = str(raw_input())
    print "Case #{}: {}".format(i, solve(number))
