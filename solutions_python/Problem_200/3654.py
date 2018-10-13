t = int(raw_input())
for z in range(1, t + 1):
    a = [int(s) for s in raw_input()]
    f = 0
    i = 0
    while(i <= (len(a) - 2)):
        #for j in range(i + 1, len(a)):
        if(a[i] > a[i + 1]):
            a[i] = a[i] - 1
            for k in range(i + 1, len(a)):
                a[k] = 9
            f = 1
        else:
            f = 0
        i = i + 1
        if(f == 1):
            i = 0
        #if(f == 0):
        #    break
            

    s = 0
    for i in range(len(a)):
        p = (len(a) - 1) - i
        s = s + (a[i] * (10 ** p))
    print "Case #{}: {}".format(z, s)
    
