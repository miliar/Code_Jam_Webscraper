fin = open("A-large.in","rt")
fout = open("OUTPUT.txt","wt")

t = fin.readline().rstrip('\n')
t = int(t)

for case in range(1,t+1):
    n = fin.readline().rstrip('\n')
    n = n.split(" ")
    d = int(n[0])
    n = int(n[1])
    time = 0
    for horse in range(n):
        k = fin.readline().rstrip('\n')
        k = k.split(" ")
        s = int(k[1])
        k = int(k[0])
        dtogo = d-k
        if dtogo < 0: continue
        ntime = float(dtogo)/float(s)
        if ntime > time: time = ntime
    sout = "Case #"+str(case)+": "
    sout += str( float(d)/time )
    print sout
    fout.write(sout+'\n')

fout.close()
