C=int(raw_input())
for i in range(C):
    w = raw_input()
    a, b = [int(j) for j in w.split()]
    #ans = "ON"
    #for k in range(a):
        #if b & 1 == 0:
            #ans = "OFF"
            #break
        #b >>= 1

    ans = "ON" if (b+1)%(1<<a)==0 else "OFF"

    print 'Case #%d: %s' % (i+1, ans)

