def getresult():
    s = input()

    cakes = s.split()[0]
    k = int(s.split()[1])
    
    c = [False]*len(cakes)
    for i in range(len(cakes)):
        if(cakes[i] == '+'):
            c[i] = True

    was = set()
    was.add(tuple(c))

    def iscorrect(c):
        return c.count(False) == 0

    result = 0
    while(not iscorrect(c)):
        firstminus = 0
        while(c[firstminus]):
            firstminus += 1
        firstminus = min(firstminus, len(c) - k)
        for i in range(firstminus, firstminus + k):
            if c[i]:
                c[i] = False
            else:
                c[i] = True
        if(tuple(c) in was):
            result = -1
            break
        was.add(tuple(c))
        result += 1
    if(result == -1):
        return "IMPOSSIBLE"
    return str(result)

t = int(input())
for i in range(t):
    print("Case #" + str(i + 1) + ": " + getresult()) 
