with open("A-small-attempt1.in","r") as f:
    numOfCase = int(f.readline())
    print(numOfCase)
    for i in range(numOfCase):
        ans = 0
        currentStander = 0
        lines = f.readline().split()
        smax = int(lines[0])
        audience = lines[1]
        for j in range(smax+1):
            if(currentStander >= j):
                currentStander += int(audience[j])
            elif (int(audience[j]) > 0):
                ans += (j-currentStander)
                currentStander += ans+int(audience[j])
        print("Case #%d: %d" % (i+1,ans))
f.closed
