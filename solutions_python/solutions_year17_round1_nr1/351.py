t = input()

def fillAdjacents(array, index):

    i = index - 1

    while i >= 0:
        if array[i] == "?":
            array[i] = array[index]
            i -= 1
        else:
            break
    i = index + 1

    while i < len(array):
        if array[i] == "?":
            array[i] = array[index]
            i += 1
        else:
            break

    return array

p = 0
while t:
    t -= 1
    p += 1
    m,n = raw_input().split()
    m = int(m)
    n = int(n)
    i = 0
    cakes =[]
    while i < m:
        i += 1
        temp = raw_input()
        temp = list(temp)
        cakes.append(temp)

    i = 0
    print "Case #" + str(p) + ":"
    previousCount = 0
    previousCorrectArray = None
    while i < m:
        temp = cakes[i]

        j = 0
        while j < n:

            if temp[j] != "?":
                temp = fillAdjacents(temp, j)

            j += 1
        if temp.count("?") == n:
            if previousCorrectArray != None:
                print ''.join(previousCorrectArray)
            else:
                previousCount += 1

        else:
            previousCorrectArray = temp
            if previousCount > 0:
                while previousCount:
                    previousCount -= 1
                    print ''.join(temp)

            print ''.join(temp)
        i += 1