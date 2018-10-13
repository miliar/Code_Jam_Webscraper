from collections import deque

def countFlips(cakes, flipper):
    cakes = list(cakes)

    queue = deque()
    queue.append((cakes, 0))

    hashSet = set()

    while len(queue) > 0:
        cakeState = queue.popleft()
        if isHappy(cakeState[0]):
            return cakeState[1]

        hashSet.add(makeString(cakeState[0]))

        numFlips = cakeState[1] + 1

        for i in range(0, len(cakeState[0]) - flipper + 1):
            newCakeState = flip(cakeState[0], i, flipper)
            if makeString(newCakeState) not in hashSet:
                queue.append((newCakeState, numFlips))

    return "IMPOSSIBLE"

def flip(cakes, flipIndex, flipLength):
    flippedCakes = list(cakes)
    for i in range(flipIndex, flipIndex + flipLength):
        if flippedCakes[i] == '+':
            flippedCakes[i] = '-'
        else:
            flippedCakes[i] = '+'

    return flippedCakes

def isHappy(cakes):
    for c in cakes:
        if c == '-':
            return False
    
    return True

def makeString(cakeState):
    return ''.join(cakeState)

t = int(input())

for i in range(1, t + 1):
    line = input().split(' ')
    S = line[0]
    K = int(line[1])
    print('Case #{}: {}'.format(i, countFlips(S, K)))