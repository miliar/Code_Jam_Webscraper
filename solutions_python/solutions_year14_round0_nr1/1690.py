def tellCard(r1,r2,a1,a2,t):
    i = 0
    ans = []
    r1 -= 1
    r2 -= 1
    while i < 4:
        if a1[r1][i] in a2[r2]:
            ans.append(a1[r1][i])
        i += 1
    if len(ans) == 1:
        print "Case #" + str(t) + ": " + str(int(ans[0]))
    elif len(ans) > 1:
        print "Case #" + str(t) + ": Bad Magician!"
    elif len(ans) == 0:
        print "Case #" + str(t) + ": Volunteer cheated!"
        
f = open("a.txt", "r", 0)
t = int(f.readline())
i = 0
while i < t:
    a1 = []
    a2 = []
    r1 = int(f.readline())
    j = 0
    while j < 4:
        a1.append(f.readline().split(' '))
        j += 1
    r2 = int(f.readline())
    j = 0
    while j < 4:
        a2.append(f.readline().split(' '))
        j += 1
    
    m = 0
    while m < 4:
        n = 0
        while n < 4:
            a1[m][n] = int(a1[m][n])
            n += 1
        m += 1
        
    m = 0
    while m < 4:
        n = 0
        while n < 4:
            a2[m][n] = int(a2[m][n])
            n += 1
        m += 1
    tellCard(r1,r2,a1,a2,i+1)
    i += 1