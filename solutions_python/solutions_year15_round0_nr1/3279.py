f = open("A-large.in")
cases = int(f.readline())
for n in range(1,cases+1):
    [sMax,stats] = f.readline().split()
    smax=int(sMax)
    confidince = dict()
    for i in range(smax+1):
        confidince[i]=int(stats[i])
    standers = 0
    extras = 0
    for s in confidince.keys():
        if standers < s:
            needed = s - standers
            extras += needed
            standers+= needed
        standers += confidince[s]
    print ("Case #"+str(n)+": "+str(extras))
