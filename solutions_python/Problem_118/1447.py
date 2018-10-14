from math import ceil, sqrt, floor

def fair_and_square(n):
    str_n = str(n)
    str_n_sq = str(n * n)
    return str_n == str_n[::-1] and str_n_sq == str_n_sq[::-1]

n = raw_input()
for i in xrange(int(n)):
    interval = raw_input()
    interval = interval.split(" ")
    # print interval
    s = 0
    for x in xrange(int(ceil(sqrt(int(interval[0])))), int(ceil(sqrt(int(interval[1]) + 1)))):
        s += fair_and_square(x)
        # print x
        # if fair_and_square(x):
        #     print "%d is fair and square!" % x
        #     s += 1
    print "Case #%d: %d" % (i + 1, s)

print ""