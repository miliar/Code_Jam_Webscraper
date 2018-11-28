import sys

name = "B-large"
path = ""
sys.stdin = open(path+name+".in")
sys.stdout = open(path+name+".out", 'w')
testCases = int(input())

def isTidy(num):
    for rIndex in range(len(num)-2, -1, -1):
        left = num[rIndex]
        right = num[rIndex+1]
        if int(left) > int(right):
            num[rIndex] = str(int(left)-1)
            for index in range(rIndex+1, len(num)):
                num[index] = '9'
    return num


for testCase in range(1, testCases+1):
    N = input()
    tidy = isTidy(list(N))
    x = ''.join(tidy)
    print("Case #{}: {}".format(testCase, int(x)))
