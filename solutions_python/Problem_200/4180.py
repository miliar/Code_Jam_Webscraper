def is_tidy(n):
    if n <= 0: return 0
    arr = [int(d) for d in str(n)]
    end = len(arr) - 1
    for i in xrange(0, end):
        if arr[end - 1 - i] > arr[end - i]:
            return 0

    #print "is tidy %s" % n
    return 1
#132 -> 129
#434 -> 399
#1000
#111111111111111110
def find(n):
    arr = [int(d) for d in reversed(str(n))]
    end = len(arr) - 1
    for i in xrange(0, end):
        if arr[i] <= arr[i + 1]:
            return arr[i] + 1

        j = i
        while j + 1 > end or arr[j] > arr[j + 1]:
            j += 1

        num = 0
        for x in range(i,j + 1):
            num += arr[x] * 10**x

        #print "subtracting %s" % num
        return num

for i in xrange(1,1+input()):
    s = int(raw_input())

    #print "start %s" % s

    while s >= 0 and not is_tidy(s):
        s -= 1 #find(s)
        #print "s is %s " % s

    if s > 0:
        print "Case #%s: %s" % (i, s)
