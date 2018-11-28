# -*- coding: utf-8 -*-


def toBinList(x):
    powers = []
    while x != 0:
        powers.append(x % 2)
        x /= 2
    return powers

data = open('C.in', 'r').read().split('\n')
output = open('C.out', 'w')

T = int(data.pop(0))

for t in range(T):
    N = int(data.pop(0))
    candies = map(int, data.pop(0).split(' '))
    binaries = map(toBinList, candies)
    lengths = map(len, binaries)
    maxLength = reduce(max, lengths)

    #1s in pos i
    ans = 'YES'
    for i in range(maxLength):
        ones = 0
        for binary in binaries:
            if len(binary)-1 >= i:
                if binary[i] == 1:
                    ones += 1
        if ones % 2 != 0:
            ans = 'NO'


    if ans == 'YES':
        minCandie = min(candies)
        totalSum = sum(candies)
        sean = totalSum - minCandie
        ans = str(sean)
    print 'Case #' + str(t+1) + ': ' + ans
    output.write('Case #' + str(t+1) + ': ' + str(ans) + '\n')
output.close()
