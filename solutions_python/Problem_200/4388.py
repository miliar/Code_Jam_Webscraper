def minusOne(char):
    if char == '0':
        return '9'
    else:
        return str(int(char) - 1)


def isTidy(num):
    for i, char in enumerate(num):
        if i + 1 < len(num):
            if int(char) > int(num[i + 1]):
                return False
    return True


def removeZeros(num):
    i = 0
    while num[i] == '0':
        i += 1
    return num[i:]


def arrangeNum(num, idx):
    num = num[:idx] + '9' + num[idx + 1:]
    i = 1
    if num[idx - 1] == '0':
        while num[idx - i] == '0' and not idx - 1 < 0:
            num = num[:idx - i] + minusOne(num[idx - i]) + num[idx - i + 1:]
            i += 1
    if idx - i >= 0:
        num = num[:idx - i] + minusOne(num[idx - i]) + num[idx - i + 1:]
    num = removeZeros(num)
    return num


fileName = 'B-large.in'
outputFile = 'B-large.out'
output = []
with open(fileName, 'r') as f:
    t = int(f.readline().strip())
    for n in range(t):
        num = f.readline().strip()
        i = len(num) - 1
        while not isTidy(num):
            num = arrangeNum(num, i)
            i -= 1
        output.append('Case #%s: %s\n' % (n + 1, num))

with open(outputFile, 'w') as f:
    f.writelines(output)
