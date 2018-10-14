__author__ = 'fabrizio'

with open("input.txt") as fin:
    with open("output.txt","w") as fout:
        T=int(fin.readline().strip())
        for t in range(1,T+1):
            N=int(fin.readline().strip())
            naomi=sorted(map(float,fin.readline().strip().split()),reverse=True)
            ken=sorted(map(float,fin.readline().strip().split()))
            naomi_copy=naomi[:]
            ken_copy=ken[:]

            war=N
            for na in naomi:
                remove=None
                for ke in ken:
                    if ke>na:
                        remove=ke
                        break
                if remove is not None:
                    ken.remove(remove)
                    war-=1
                else:
                    ken=ken[1:] #least

            naomi=naomi_copy
            ken=ken_copy
            d_war=N
            for i in range(N):
                told_ken=naomi[0] #greatest
                remove_ken=None
                for ke in ken:
                    if ke>told_ken:
                        remove_ken=ke
                        break
                if remove_ken is not None:
                    #ken win
                    ken.remove(remove_ken)
                    #remove least naomi
                    naomi=naomi[:-1]
                    d_war-=1
                else:
                    #ken lost
                    remove_ken=ken[0]
                    ken=ken[1:] #least used
                    #remove naomi win but least
                    remove_naomi=None
                    for na in reversed(naomi): #sorted
                        if na>remove_ken:
                            remove_naomi=na
                            break
                    if remove_naomi is not None:
                        naomi.remove(remove_naomi)
                    else:
                        naomi.remove(told_ken)

            print "Case #%s: %s %s"%(t,d_war,war)
            fout.write("Case #%s: %s %s\n"%(t,d_war,war))



