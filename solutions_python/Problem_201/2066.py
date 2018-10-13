t = int(input().strip()) # num testcases
for c in range(t):
    n,k = map(int,input().strip().split()) # n = num stalls (+ 2 on each end for guard) ; k = num people enter room
    if n == k: # all stalls filled
        print("Case #" + str(c + 1) + ": 0 0")
    elif k == 1: # one stall
        if n % 2 == 1:
            print("Case #" + str(c + 1) + ": " + str(n // 2), str(n // 2))
        else:
            print("Case #" + str(c + 1) + ": " + str(n // 2), str((n-1) // 2))
    elif k >= n*0.7:
        print("Case #" + str(c + 1) + ": 0 0")
    else: # grind the answer
        array = [0] * (n + 2)   # keep track of stalls
        array[0] = 1
        array[-1] = 1
        for i in range(k):   # place persons in stalls one at a time
            minDist = 0   # min(Ls,Rs) is maximal
            tempMaxDist = 0
            for j in range(1,len(array)-1):   # check Ls and Rs of each stall
                left = 0
                right = 0
                if array[j] != 1:
                    index = j - 1
                    while index >= 0:
                        if array[index] == 0:
                            left += 1
                            index -= 1
                        else:
                            break
                    index = j + 1
                    while index < len(array):
                        if array[index] == 0:
                            right += 1
                            index += 1
                        else:
                            break
                    # print(left,right, min(left,right))
                    minDist = max(minDist,min(left,right))
                    tempMaxDist = max(tempMaxDist,max(left,right))
            #print("minDist:",minDist,i) #TEST
            if tempMaxDist == 0:
                print("Case #" + str(c + 1) + ": 0 0")
                break
            maxDist = 0   # max(Ls,Rs) is maximal
            indexChange = 0
            for j in range(len(array)-1,0,-1):
                left = 0
                right = 0
                if array[j] != 1:
                    index = j - 1
                    while index >= 0:
                        if array[index] == 0:
                            left += 1
                            index -= 1
                        else:
                            break
                    index = j + 1
                    while index < len(array):
                        if array[index] == 0:
                            right += 1
                            index += 1
                        else:
                            break
                    if min(left,right) == minDist and maxDist <= max(left,right):
                        maxDist = max(left,right)
                        indexChange = j
                        
            #print(indexChange)
            if i == k - 1:   # this is last person, print his max and min
                array[indexChange] = 1
                print("Case #" + str(c + 1) + ": " + str(maxDist), str(minDist))
                #break
            else:
                array[indexChange] = 1
