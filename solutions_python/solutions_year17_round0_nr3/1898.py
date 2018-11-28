import math

def main():
    t = int(raw_input())

    result = []


    for i in xrange(t):
        n = raw_input()

        entry = n.split()
        n = int(entry[0])
        k = int(entry[1])

        stalls = ['o']

        for j in xrange(1, n+2):   #presta atencao
            if j == n+1:
                stalls.append('o')
            else:
                stalls.append(None)

        for y in xrange(k):
            minIndex, maxIndex = findEmpty(stalls)
            place = math.floor((maxIndex-minIndex)/2)+minIndex
            stalls[int(place)] = 'o'


        lastPersonLeft = int(place) - minIndex
        lastPersonRight = maxIndex - int(place)

        if lastPersonRight >= lastPersonLeft:
            result.append([lastPersonRight,lastPersonLeft])
        else:
            result.append([lastPersonLeft, lastPersonRight])

    for p in range(t):
        print 'Case #'+str(p+1)+': '+str(result[p][0])+' '+str(result[p][1])


def findEmpty(stalls):
    count = 0
    maxFree = 0
    minIndex = 0
    maxIndex = 0

    for i in range(len(stalls)):
        if stalls[i] == None:
            count += 1
        elif(maxFree<count):
            maxFree = count
            maxIndex = i-1
            minIndex = i-maxFree
            count = 0
        else:
            count = 0

    return minIndex, maxIndex

main()