# codado por tony

def checkTidy(num):
    num = list(str(num))
    i = len(num) - 1
    while(i > 0):
        if(num[i] < num[i-1]):
            niner(num, i)
            num[i-1] = str(int(num[i-1]) - 1)
        i -= 1
    removeZero(num)
    return ''.join(str(x) for x in num)

def removeZero(num):
    while(num[0] == '0'):
        num.pop(0)
    return

def niner(num, i):
    max = len(num)
    while(i < max and num[i] != 9):
        num[i] = 9
        i += 1

cases = int(input())
for i in range(1, cases+1):
    num = input()
    print("Case #" + str(i) + ": " + checkTidy(num))
