
t = int(raw_input())
for case in range(1, t+1):

    [a, k] = raw_input().split()
    k = int(k)
    #print k
    s = len(a)
    a = list(a)
    count = 0
    #print "=========%s=======" % case 
    for i in range(0, s-k+1):
        if a[i] == "-":
            count +=1
            for j in range(i, i+k):
                if a[j] == '-':
                    a[j] = '+'
                else:
                    a[j] = '-'
       # print ''.join(a)                
    if '-' not in a:
        print "Case #%s: %s" % (case, count)
    else:
        print "Case #%s: IMPOSSIBLE" % (case)
