import itertools

def tryIt(intList):
    sums = []
    myList = []
    for i in xrange(1,20):
        tmp = itertools.combinations(intList, i)
        for j in tmp:
            myList += [j]
            sum = 0
            for l in j:
                sum += int(l)
            if sum in sums:
                returnValue = []
                returnValue += [j]
                returnValue += [myList[sums.index(sum)]]
                return returnValue
            sums += [sum]
        
    return []


fi = open('input', 'r')
fo = open('output', 'w')
T = int(fi.readline())
for caseCnt in xrange(0,T):
    input = fi.readline().split(' ')
    N = int(input[0])
    intList = []
    for i in xrange(1, N+1):
        intList += [int(input[i])]
    
    result = tryIt(intList)
    fo.write("Case #" + str(caseCnt+1)+":\n")
    if result == []:
        fo.write("Impossible\n")
    else:
        fo.write(" ".join(str(n) for n in result[0]) + "\n")
        fo.write(" ".join(str(n) for n in result[1]) + "\n")
        

    
    