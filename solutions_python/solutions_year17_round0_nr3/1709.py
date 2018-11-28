def BathroomStalls():
    N = map(int, raw_input().strip().split())

    
    # temp1 = findParent(N[0], N[1])

    list = [N[0]]

    i = list[0]

    index = 0 

    while i != 0:
        i = list[index]

        list.append(i/2)
        list.append(i - (i/2) -1)

        index+=1
    list = sorted(list)

    temp1 = list[len(list)- N[1]]
    result = []
    result.append(temp1/2)
    if temp1%2 == 0: 
        result.append(max(temp1/2 - 1, 0))
    else: 
        result.append(temp1/2)

    # if temp1%2 == 0:
    #     result.append(temp1/2-1)
    # else:
    #     result.append(temp1/2)

    return result

def findParent(a, b):
    if b == 1:
        return a

    c = findParent(a, b/2)

    if c%2 == 0: 
        if b%2 == 1:
            return c/2 - 1

    return c/2


for case in xrange(input()):
    result = BathroomStalls()
    # print result
    print 'Case #%d: %d %d' % (case+1,result[0], result[1] )
