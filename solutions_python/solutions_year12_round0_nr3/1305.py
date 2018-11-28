from math import log10, pow, floor

f = open("q3.in", "r")
n = int(f.readline().strip())
for i in xrange(0, n):
    used = {}
    a, b = map(int, f.readline().split())
    count = 0
    for j in xrange(a, b+1):
        num_digits = int(floor(log10(j)) + 1)
        top_power_of_ten = int(pow(10, num_digits-1))
        num = j
        for k in xrange(0, num_digits):
            num = num / 10 + top_power_of_ten * (num % 10)
            if used.get((j, num), None) == None and num > j and num <= b:
                count+=1
                used[(j, num)] = 1
    print "Case #%d: %d" % (i+1, count)
