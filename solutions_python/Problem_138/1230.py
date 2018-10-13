infile = open("D-large.in","r")
outfile = open("D-large.out","w")

cases = int(infile.readline())

for x in range(cases):
    #reset
    y = 0
    z = 0
    
    #read case
    N = int(infile.readline())
    naomi = infile.readline().split()
    ken = infile.readline().split()
    
    #convert to numbers & sort
    for b in range(N):
        naomi[b] = float(naomi[b])
        ken[b] = float(ken[b])
    
    naomi.sort()
    ken.sort()
    
    naomi2 = naomi[:]
    ken2 = ken[:]
    
    # y: deceitful war optimal
    for t in range(N):
        if max(naomi) < min(ken):
            break
        elif min(naomi) > max(ken):
            y += len(naomi)
            break
        elif min(naomi) < min(ken):
            naomi.remove(min(naomi))
            ken.remove(max(ken))
        else: #min(naomi) > min(ken)
            naomi.remove(min(naomi))
            ken.remove(min(ken))
            y+= 1
    
    # z: war optimal
    naomi2.reverse()
    for t in range(N):
        if max(naomi2) > max(ken2):
            naomi2.remove(max(naomi2))
            ken2.remove(min(ken2))
            z+=1
        else: #max(naomi2) < max(ken2)
            naomi2.remove(max(naomi2))
            ken2.remove(max(ken2))
    
    case = x + 1
    if case == cases:
        outfile.write("Case #%d: %d %d" % (case, y, z))
    else:
        outfile.write("Case #%d: %d %d\n" % (case, y, z))
    
infile.close()
outfile.close()