def findNotTydy(number):
    s = str(number)
    for i in xrange(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            return i + 1
    return 0


t = int(raw_input())

for i in xrange(1, t + 1):
    num = int(raw_input())
    n = findNotTydy(num)
    while n:
        k = (len(str(num)) - n)
        num -= num % 10 ** k + 1
        n = findNotTydy(num)

    print "Case #{}: {}".format(i, num)
