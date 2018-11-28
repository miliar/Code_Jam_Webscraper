import heapq
#t = input()
#for poo in range(t):
#    n, k = map(int, raw_input().split())
#    l = [-n]
#    a = 0
#    b = 0
#    for i in range(k):
#        top = -heapq.heappop(l)
#        top -= 1
#        a = top / 2
#        b = top - a
#        heapq.heappush(l, -a)
#        heapq.heappush(l, -b)
#    print "Case #" + str(poo+1) + ":", max(a, b), min(a, b)

#n = 22
#for k in range(1, n+1):
#    l = [-n]
#    a = 0
#    b = 0
#    for i in range(k):
#        top = -heapq.heappop(l)
#        top -= 1
#        a = top / 2
#        b = top - a
#        heapq.heappush(l, -a)
#        heapq.heappush(l, -b)
#    print "Case #" + str(k) + ":", max(a, b), min(a, b)

t = input()
for poo in range(t):
    n, k = map(int, raw_input().split())
    p = 0
    num1 = (n)/2
    num2 = num1-1
    count1 = 2 if (n%2 == 1) else 1
    count2 = 2 - count1
    # 2^p <= k < 2^(p+1)
    while not((1<<p) <= k and k < (1<<(p+1))):
        new_num1 = num1 / 2
        new_num2 = new_num1 - 1
        new_count1 = 0
        new_count2 = 0
        a = (num1 - 1) / 2
        b = (num1 - 1) - a
        if a == new_num1:
            new_count1 += count1
        elif a == new_num2:
            new_count2 += count1
        if b == new_num1:
            new_count1 += count1
        elif b == new_num2:
            new_count2 += count1
        a = (num2 - 1) / 2
        b = (num2 - 1) - a
        if a == new_num1:
            new_count1 += count2
        elif a == new_num2:
            new_count2 += count2
        if b == new_num1:
            new_count1 += count2
        elif b == new_num2:
            new_count2 += count2
        num1 = new_num1
        num2 = new_num2
        count1 = new_count1
        count2 = new_count2
        p += 1
    res = k - (1<<p) + 1
    print "Case #" + str(poo+1) + ":",
    if count2 > count1:
        if res <= count1:
            print num1, num2
        else:
            print num2, num2
    else:
        if res <= ((1<<p)-count2):
            print num1, num1
        else:
            print num1, num2

