T = int(raw_input())
for test in range(T):
    _, shys = raw_input().split()
    shys = map(int, shys)
    #print shys
    total_added = 0
    total = 0
    for i, s in enumerate(shys):
        added = max(i - total, 0) 
        total_added += added
        total += added
        total += s
    print 'Case #%d: %d' % (test+1, total_added)



        

