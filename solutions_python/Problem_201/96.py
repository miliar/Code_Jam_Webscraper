
T = int(raw_input())  
for K in xrange (T):
    n, k = [int(g) for g in raw_input().split(" ")]

    dic = {n:1}
    first = n
    while (k > dic[first]):
        k -= dic[first]

        left = (first - 1) / 2
        right = left + (first % 2 == 0)
        if (left > 0):
            if (left not in dic):
                dic[left] = 0
            dic[left] += dic[first]
        if (right > 0):
            if (right not in dic):
                dic[right] = 0
            dic[right] += dic[first]

        del dic[first]
        first = max(dic.keys())
        #print k, dic


    left = (first - 1) / 2
    right = left + (first % 2 == 0)
    print "Case #{}: {} {}".format(K+1, right, left)

    