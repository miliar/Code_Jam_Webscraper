def subtract(num, index, length):
    num[index] = num[index] - 1
    for i in range(index+1, length):
        num[i] = 9
    return num

def subtract2(num, index):
    for i in range(index, 0, -1):
        if((i-1) != -1):
            if(num[i] < num[i-1]):
                num[i] = 9
                num[i-1] = num[i-1] - 1
    return num


numCases = int(input())
for i in range(1, numCases+1):
    num = list(map(int, str(input())))
    changedIndex = 0
    numLength = len(num)

    for index in xrange(numLength):
        if ((index + 1) != numLength):
            if (num[index] >  num[index+1]):
                num = subtract(num, index, numLength)
                changedIndex = index
                index = numLength

    if(changedIndex != 0):
        num = subtract2(num, changedIndex)

    print('Case #{}: {}').format(i, int(''.join(map(str,num))))
