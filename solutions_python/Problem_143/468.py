infile = open("B-small-attempt0.in", "rU")
outfile = open("B.out", "w")

ncases = int(infile.readline())

def largest_power_of_2(n):
    a = 1
    p = -1

    while a <= n:
        a *= 2
        p += 1

    return p 

for case in xrange(1, ncases+1):
    a, b, k = [int(x) for x in infile.readline().strip().split(" ")]

    total = 0
    
    for i in xrange(0, a):
        for j in xrange(0, b):
            if (i&j) < k:
                total += 1

    outfile.write("Case #%d: %d\n" % (case, total))

# For 0 <= k <= A, B <= 2^n, f(A, B, k) = 3^(n - 1s in binary expansion of k)
# For 0 it's that minus 2x-1

##listy = []
##x = 8
##for a in xrange(1, x):
##    for b in xrange(1, x):
##        listy.append(a & b)
##
##tup = {}
##
##for i in listy:
##    if i not in tup:
##        tup[i] = listy.count(i)
##
##for i in xrange(x):
##    total = 0
##
##    for j in xrange(i+1):
##        total += tup[j]
##
##    print i, total
    
infile.close()
outfile.close()
