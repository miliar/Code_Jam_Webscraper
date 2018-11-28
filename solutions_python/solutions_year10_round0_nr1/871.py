input = open("A-large.in")

length = int(input.readline())

problems = []
for l in input:
    problems.append(l.split())

i = 1
for p in problems:
    n = int(p[0])
    k = int(p[1])
    if k > 0 and (k+1) % 2**n == 0:
        print "Case #%d: ON" % i
    else:
        print "Case #%d: OFF" % i
    i += 1
