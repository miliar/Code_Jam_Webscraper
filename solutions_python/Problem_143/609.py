t = input()
for i in range(t):
    a,b,k = map(int,raw_input().split())
    c = 0
    for j in range(a):
        for l in range(b):
            if (j & l) < k:
                #print j,l
                c += 1
    print 'Case #'+str(i+1)+': '+str(c)
