tests = int(raw_input())

for test in range(1, tests+1):
    num = int(raw_input())
    ten = 10
    prev = num % 10
    while num%ten != num:
        cur = (num/ten)%10
        if cur > prev:
            num = num - (num%ten) - 1
        prev = (num/ten)%10
        ten = ten * 10
    print "Case #%s: %s"%(str(test),str(num))
