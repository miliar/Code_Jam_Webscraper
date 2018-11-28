t = int(input())

for i in range(t):

    ctr = 0
    a = []
    
    q = input().split()[1]
    a.append(0)
    
    for j in range(0,len(q)):
        a.append(a[j] + int(q[j]))
    
    for j in range(1, len(a)):
        diff = j - a[j]
        if(diff > 0):
            ctr += diff

            for k in range(j, len(a)):
                a[k] += 1

    print("Case #" + str(i+1) + ": " + str(ctr))
    
