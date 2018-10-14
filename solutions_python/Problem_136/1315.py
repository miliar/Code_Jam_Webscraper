f = open("input6.in", "r")
fout = open("output2b.out", "w")
tot = f.readlines()

T = int(tot[0]) # numero di casi

indexstart = 1
i = 0

for x in range(T):
    i+=1
    shit = tot[indexstart]
    indexstart=indexstart+1
    
    shit = shit.strip().split(" ")
    cost = float(shit[0])
    fcps = float(shit[1])
    obj = float(shit[2])
    realobj=obj
    cps = 2.0
    totaltime = 0.0

    while(1):
        if(cost/cps+(obj)/(cps+fcps) > obj/cps):
            totaltime+=obj/cps
            break
        else:
            totaltime+=cost/cps
            #print cost/cps
            cps+=fcps
    #print totaltime
    fout.write("Case #{0}: {1}\n".format(i, totaltime))
fout.close()
f.close()






