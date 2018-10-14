#functions
def flip(cakes, index, size):
    for i in range(index, (index+size)):
        if (cakes[i] == '+'):
            cakes[i] = '-'
        else:
            cakes[i] = '+'
    return cakes

def allHappy(cakes):
    for i in xrange(len(cakes)):
        if (cakes[i] == '-'):
            return False;
    return True;

numCases = int(input())
for i in range(1, numCases+1):
    cakes, size = raw_input().split(' ')
    cakes = list(cakes)
    size = int(size)

    numFlips = 0
    for index in range (0, (len(cakes)-size+1)):
        if (cakes[index] == '-'):
            cakes = flip(cakes, index, size)
            numFlips+=1

    response = "IMPOSSIBLE"
    if (allHappy(cakes)):
        response = numFlips

    print("Case #{}: {}").format(i, response)
