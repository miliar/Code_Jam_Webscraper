T = int(raw_input())

for n in range(T):
    arr = raw_input().split()
    N,S,p = map(int,arr[0:3])
    
    arr2 = [(int(t)/3, int(t)%3) for t in arr[3:]]
    
    count = len([i for i in arr2 if (i[0] >= p) or (i[0] == p-1 and i[1] > 0)])
    #print count, len([i for i in arr2 if (i[1] == 0 and i[0] == p-1) or (i[1] == 2 and i[0] == p-2)])
    count = count + min(len([i for i in arr2 if (i[1] == 0 and i[0] == p-1 and i[0] > 0) or (i[1] == 2 and i[0] == p-2)]), S)
    print 'Case #%d: %d' % (n+1, count)
    