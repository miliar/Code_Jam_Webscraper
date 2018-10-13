def getNext(index):

    if countMap.has_key(index):
        countMap[index] -= 1
        if countMap[index] == 0:
            del countMap[index]
        return index
    else:
        index = max(countMap.keys())
        countMap[index] -= 1
        if countMap[index] == 0:
            del countMap[index]
        return index

def getAndRemoveNextCount():
    index = max(countMap.keys())
    count = countMap[index]
    del countMap[index]
    return index, count


tc = input()

i = 1

countArray = []
countMap = {}

while tc:
    tc -= 1
    n, k = raw_input().split()
    n = int(n)
    k = int(k)

    if k == n:
        print "Case #" + str(i) + ": 0 0"
        i += 1
        continue

    t = n
    l = [t]
    countMap = {}


    temp = t
    result = []
    previous = t
    totalCount = 0
    countMap[t] = 1
    while temp != 0:
        #temp = getNext(previous)

        if totalCount >= k:
            break


        temp, count = getAndRemoveNextCount()

        totalCount += count

        result.append({"number": temp, "count": count})
        #result = result + ([temp] * count)
        num1 = temp/2 - (temp + 1)%2
        num2 = temp/2
        if (countMap.has_key(num1)):
            countMap[num1] += count
        else:
            countMap[num1] = count

        if (countMap.has_key(num2)):
            countMap[num2] += count
        else:
            countMap[num2] = count

    p = 0
    length = len(result)
    count = 0
    while p < length:
        count += result[p]["count"]
        if count > k:
            temp = result[p]["number"]
            break
        p += 1


    if temp == 0:
        print "Case #" + str(i) + ": 0 0"
    else:
        print "Case #" + str(i) + ": " + str(temp/2) + " " + str(temp/2 - (temp + 1)%2)
    i += 1
