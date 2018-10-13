f=open("input.txt")
cases=int(f.readline())
for i in xrange(0,cases):
    n=int(f.readline())
    digits=[int(a) for a in f.readline().split(" ")]
    min = sum = xor = 0
    for digit in digits:
        if digit < min or min == 0: min = digit
        sum += digit
        xor = xor ^ digit
    if xor == 0: print "Case #%d: %d"%(i+1, sum-min)
    else: print "Case #%d: %s"%(i+1, "NO")
f.close()