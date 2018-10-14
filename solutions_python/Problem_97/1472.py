import sys

def recycle(a,b):

    integers = [i for i in xrange(a,b+1)]
    numbs = dict()

    for i in integers:
        numbs[i] = cycle(str(i))

    count = 0
#    print numbs
    for x in xrange(0,len(integers)):
        for y in xrange(x+1, len(integers)):
            if integers[y] in numbs[integers[x]]:
                count+=1
                continue
#            if k == l: continue

#            if k < l:
#                if l in numbs[k]:
#                    count+=1
##                    print k,l
#                    continue
    return count

def cycle(x):
    length = len(x)-1
    result = []


    while length > 0:
        temp = x[length:]
        if temp[0] != '0': result.append(int(temp + x[:length]))
        length -= 1
    print result
    return result

if __name__ == "__main__":
    f = sys.stdin
    output = open('C-small.txt', 'w')
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    test = int(f.readline())
    for t in xrange(test):
        n = f.readline().split()
        print n
        output.write("Case #%d: %d \n" % (t+1, recycle(int(n[0]), int(n[1]))))

    output.close()
#if __name__ == "__main__":
#    print recycle(100, 500)