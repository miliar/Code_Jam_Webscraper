import math

t = int(input())

for i in range(t):

    n = int(input())
    pie = input().split()

    a = dict()

    for l in pie:
        try:
            a[int(l)] += 1
        except:
            a[int(l)] = 1
            
    flag = 0
    ctr = 0
    keymax = max(a.keys(), key=int)
    
    while(flag == 0):
        j = max(a.keys(), key=int)

        if(math.ceil(j/2) + a[j] < j):
            
            try:
                a[math.ceil(j/2)] += a[j]
            except:
                a[math.ceil(j/2)] = a[j]

            try:
                a[math.floor(j/2)] += a[j]
            except:
                a[math.floor(j/2)] = a[j]
        
            ctr += a[j]
            a.pop(j, None)
        else:
            flag = 1
            
    ans = max(a.keys(), key=int) + ctr

    if(keymax == 9):
        a = dict()

        for l in pie:
            try:
                a[int(l)] += 1
            except:
                a[int(l)] = 1
                
        flag = 0
        ctr = 0

        while(flag == 0):
            j = max(a.keys(), key=int)

            if(math.ceil(j/2) + a[j] < j):
                if j == 9:
                    try:
                        a[6] += a[j]
                    except:
                        a[6] = a[j]

                    try:
                        a[3] += a[j]
                    except:
                        a[3] = a[j]
                else:
                    try:
                        a[math.ceil(j/2)] += a[j]
                    except:
                        a[math.ceil(j/2)] = a[j]

                    try:
                        a[math.floor(j/2)] += a[j]
                    except:
                        a[math.floor(j/2)] = a[j]
            
                ctr += a[j]
                a.pop(j, None)
            else:
                flag = 1
            
    ans1 = max(a.keys(), key=int) + ctr

    print("Case #" + str(i+1) + ": " + str(min(ans, ans1)))
