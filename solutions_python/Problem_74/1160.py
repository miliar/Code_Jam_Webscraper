f = open("c:\codejam\A-large.in","r")
fout = open("c:\codejam\A-large-out.txt","w")
cases = int(f.next())
for case in range(cases):
    oloc = (1, 1) #location, at start of second
    bloc = (1, 1)
    raw = f.next().strip().split(' ')
    buttons = int(raw[0])
    path = raw[1:]
    #print path
    for i in range(buttons):
        color = path[2*i]
        loc = int(path[2*i+1])
        if color == "O":
            time = oloc[1] + (abs(loc - oloc[0]) + 1)
            if time < bloc[1] + 1:
                time = bloc[1] + 1
            oloc = (loc, time)
            #print "O:", oloc[0], oloc[1]
        else:
            time = bloc[1] + (abs(loc - bloc[0]) + 1)
            if time < oloc[1] + 1:
                time = oloc[1] + 1
            bloc = (loc, time)
            #print "B:", bloc[0], bloc[1]
    totaltime = max((oloc[1],bloc[1]))-1
    fout.write("Case #%d: %d\n" % (case + 1,totaltime))
f.close()
fout.close()
