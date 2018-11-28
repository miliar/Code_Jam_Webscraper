f = open("input.txt", "r")
fout = open("output.txt", "w")
tot = f.readlines()
L = tot[0]
i = 0
while(i<int(L)):
    i+=1
    line = tot[i].split()
    #print line
    N = int(line[0]) # number of googlers
    S = int(line[1]) # surprising
    p = int(line[2]) # limit to reach of single
    points = []
    ok = 0
    for x in range(3, (N)+3):
        points.append(int(line[x]))
    points.sort()
    #print points
    for n in points:
        if(n==0 and p>0):
            continue
        elif((n+2)/3 >= p):
            ok+=1
        elif(((n+4)/3 >= p) and (S>0)):
            ok+=1
            S-=1
        else:
            continue # next
    fout.write("Case #" + str(i) + ": " + str(ok))
    fout.write("\n")
fout.close()
f.close()
