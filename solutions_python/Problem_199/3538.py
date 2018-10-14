t = int(raw_input())

di  = {
    '+' : '-' ,
    '-' : '+'
}

for a0 in xrange(t):
    li , k = raw_input().strip().split()
    k = int(k)
    li = list(li)
    n = len(li)
    count = 0
    for i in range(n-k+1):
        if li[i] == '-':
            count += 1
            for j in range(k) :
                li[i+j] = di[li[i+j]]
    if '-' in li :
        print "Case #" + str(a0+1) + ": " +"IMPOSSIBLE"
    else :
        print "Case #" + str(a0+1) + ": " +str(count)
