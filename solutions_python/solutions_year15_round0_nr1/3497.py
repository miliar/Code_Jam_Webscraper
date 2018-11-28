t = int(raw_input())

for j in range(t):
    smax , shyness = raw_input().split()
    smax = int(smax)
    shyness = map(int, list(shyness))
    friends = 0
    total = 0
    for i in range(len(shyness)):
        if i > total + friends:
            friends += i - total - friends 
        total += shyness[i]
    print "Case #%d: %d" % (j+1, friends)
