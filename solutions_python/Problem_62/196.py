file = open("A-large.in","r")

t = int(file.readline())
for count in range(t):
    l=[]
    n = int(file.readline())
    sec=0
    for w in range(n):
        nk = file.readline().split(" ")
        a = int(nk[0])
        b = int(nk[1])
        l.append((a,b))
    #for pos1 in len(l):
    #    for pos2 in range(pos1,len(l)):
    #        if l[pos1][0]
    for fi in l:
        for it in l:
            if (fi[0] < it[0] and fi[1] > it[1]) or (fi[0] > it[0] and fi[0] < it[0]):
                sec+=1 
           
    print "Case #%d: %d"%(count+1,sec)
file.close()