f = open('B-small-attempt0.in','r')

n = int(f.readline())

index = 1

for line in f:
    num = long(line)

    for x in xrange(num,-1,-1):
        lis = [y for y in str(x)]
        b = sorted(lis)
        if lis == b:
            print "Case #{}: {}".format(index,x)
            break
    index += 1
f.close()
