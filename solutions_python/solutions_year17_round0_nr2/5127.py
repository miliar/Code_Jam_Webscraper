

def getBig(x):
    sequence = []
    for a in x:
        sequence.append(int(a))
    big = sequence[0]
    l = len(sequence)
    for i in range(l):
        if sequence[i] >= big:
            big = sequence[i]
        else:
            return False
    return True

t = int(raw_input())  # read a line with a single integer
alist = []
for i in xrange(t):
    alist.append(int(raw_input()))  # read a list of integers, 2 in this case

la = len(alist)
for x in range(1,la+1):
    n = alist[x-1]
    while n > 0:
        if getBig(str(n)):
            print "Case #{}: {}".format(x, n)
            break
        n -= 1


    







