f = open('large.in')
line = f.readline()
line = f.readline().strip()
count = 0
while line != "" :
    count += 1
    for i in range(0,2) :
        vector = map(int, f.readline().strip().split())
        if (i==0) :
            vector0 = vector
            vector0.sort()
        else :
            vector1 = vector
            vector1.sort(reverse=True)

    res = 0
    for i,x in enumerate(vector0) :
        res += x * vector1[i]
    casestr = "Case #" + str(count) + ":"
    print casestr,res
    line = f.readline()
    
