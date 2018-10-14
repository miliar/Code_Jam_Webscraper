from heapq import heappush, heappop

# Case #1: 50 49
# Case #2: 25 24
# Case #3: 24 24
# Case #4: 12 12
# Case #5: 12 11
# Case #6: 12 11
# Case #7: 12 11
# Case #8: 6 5
# Case #9: 6 5
# Case #10: 6 5

testCases = int(input())

for testCase in range(1, testCases + 1):
    s = raw_input()
    n, k = map(int, s.split(" "))
    
    traverse = []
    r = k
    while (r>1):
        traverse.append(r%2)
        r /= 2

    for t in traverse:
        if (n%2 == 0):
            n = (n/2)-t
        else:
            n = n/2
    
    if (n%2 == 0):
        print("Case #" + str(testCase) + ": " + str(n/2) + " " + str(max((n/2)-1,0)))
    else:
        print("Case #" + str(testCase) + ": " + str(n/2) + " " + str(n/2))

    # heap = []
    # heappush(heap, -n)

    # while (k>1):
    #     p = heappop(heap)
    #     newp = -(p)/2  
    #     if (p%2 == 0):
    #         heappush(heap, -newp)
    #         heappush(heap, -(newp-1))
    #     else:
    #         heappush(heap, -newp)
    #         heappush(heap, -newp)
    #     k-=1
    # # print heap
    # p = heappop(heap)
    # newp = -(p)/2
    # if (p%2 == 0):
    #     print("Case #" + str(testCase) + ": " + str(newp) + " " + str(newp-1))
    # else:
    #     print("Case #" + str(testCase) + ": " + str(newp) + " " + str(newp))
