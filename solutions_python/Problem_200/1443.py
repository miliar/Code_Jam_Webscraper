f = open("2.in")
num_test = int(f.readline())

for iter_test in xrange(num_test):
    x = map(int, list(f.readline()[:-1]))
    
    print "Case #%d:" % (iter_test + 1),
    if len(x) == 1:
        print x[0]
        continue

    for first in xrange(len(x)):
        if first == len(x) - 1:
            break
        if x[first] > x[first + 1]:
            break
    
    if first != len(x) - 1:
        for i in xrange(first + 1, len(x)):
            x[i] = 9
        x[first] -= 1

        for i in xrange(first - 1, -1, -1):
            if x[i] > x[i+1]:
                x[i + 1] = 9
                x[i] -= 1
            else:
                break

    for first in xrange(len(x)):
        if x[first] != 0:
            break

    print "".join(map(str, x[first:]))
        
