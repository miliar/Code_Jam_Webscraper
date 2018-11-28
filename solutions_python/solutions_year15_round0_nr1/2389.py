T = int(raw_input())

for t in range(1,T+1):
    sMax, sVals = raw_input().split()
    sMax = int(sMax)
    vals = [int(x) for x in sVals]
    total = 0
    friends = 0
    for i in range(sMax + 1):
        if total < i:
            friends += i - total
            total = i
        total += vals[i]
    print "Case #" + str(t) + ":", friends
