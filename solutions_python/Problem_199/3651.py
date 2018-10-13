def flipNextCakes(lis, cake, k):
    if len(lis) - cake >= k:
        for x in range(cake, cake+k):
            if lis[x] is '+':
                lis[x] = '-'
            else:
                lis[x] = '+'
        return True
    return False

def findTries(lis, k):
    numOfTries = 0
    for cake in range(len(lis)):
        if lis[cake] is '-':
            if flipNextCakes(lis, cake, k):
                numOfTries += 1
    if lis.count('-') is 0:
        return numOfTries
    else:
        return "IMPOSSIBLE"

numOfCases = int(input())
for x in range(1, numOfCases + 1):
    inp = input()
    pancakeState, kSize = inp.split()
    pancakeState = list(pancakeState)
    kSize = int(kSize)
    print("Case #" + str(x) + ": " +    str(findTries(pancakeState, kSize)))