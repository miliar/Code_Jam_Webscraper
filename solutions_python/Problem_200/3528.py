def loadNums (lista, num):
    i = 24
    while( i >= 0):
        j = 10 ** i
        lista[i] = num // j
        num = num % j
        i -= 1

n = input()
for p in range(0, n):
    nums = [0] * 25
    load = input();
    loadNums(nums, load)
    for q in range(0, 23):
        while(nums[q] < nums[q+1]):
            load = (load - load % (10 ** (q+1)))-1
            loadNums(nums, load)
    print "Case #%d: %d" % (p+1, load)
