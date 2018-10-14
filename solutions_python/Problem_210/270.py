t = int(raw_input())
    
for i in xrange(1, t + 1):
    c,j = [int(k) for k in raw_input().split(" ")]

    sc = 0
    sj = 0

    arr = [None] * (c+j)
    for l in xrange(0,c):
        c1,c2 = [int(k) for k in raw_input().split(" ")]
        sc += c2-c1
        arr[l] = (0, c1, c2)
    
    for l in xrange(0,j):
        j1,j2 = [int(k) for k in raw_input().split(" ")]
        sj += j2-j1
        arr[c+l] = (1, j1, j2)

    arr.sort(reverse = False, key=lambda tup: tup[1])
    arr.append((arr[0][0], arr[0][1]+1440,arr[0][2]+1440))

    while(sc <= 720):
        min = 10000
        index = -1
        for z in xrange(0,len(arr)-1):
            if (arr[z][0] == 0 and arr[z+1][0] == 0):
                if (arr[z+1][1]-arr[z][2] < min):
                    index = z
                    min = arr[z+1][1]-arr[z][2]
        if (index == -1):
            break
        if (sc + min <= 720):
            sc += min
            arr[index] = (0,arr[index][1],arr[index+1][2])
            arr = arr[:index+1] + arr[index+2:]
            c-=1
        else:
            sc = 720
            break
    
    while(sj <= 720):
        min = 10000
        index = -1
        for z in xrange(0,len(arr)-1):
            if (arr[z][0] == 1 and arr[z+1][0] == 1):
                if (arr[z+1][1]-arr[z][2] < min):
                    index = z
                    min = arr[z+1][1]-arr[z][2]
        if (index == -1):
            break
        if (sj + min <= 720):
            sj += min
            arr[index] = (1,arr[index][1],arr[index+1][2])
            arr = arr[:index+1] + arr[index+2:]
            j-=1
        else:
            sj=720
            break
    
    if (sc == 720):
       print "Case #{}: {}".format(i, 2*c)
    elif (sj == 720):
       print "Case #{}: {}".format(i, 2*j)  
    else:
       print "Case #{}: {}".format(i, 2)
