def prima(sMax,audience):
    total = 0
    added = 0
    for i in range(len(audience)):
        if i > sMax:
            return added
        newAdded = i-total
        if newAdded > 0:
            added += newAdded
            total += newAdded
        total += int(audience[i])

    return added

tests = int(raw_input())
i = 0
out = open('output.txt','w')
while i<tests:
    i+=1
    r,t=raw_input().strip().split()
    r = int(r)
    out.write("Case #"+str(i)+": "+str(prima(r,t))+'\n')