fin = open ('D-large.in','r')
fout = open ('CJAM4OUT.txt','w')

T=int(fin.readline().strip())

for a in range(T):
    N = int(fin.readline().strip())
    n = list(map(float,fin.readline().strip().split()))
    k = list(map(float,fin.readline().strip().split()))
    n.sort()
    k.sort()
    fairwin = 0
    deceitwin = 0
    naomi = []
    ken = []
    
    def start():
        global naomi, ken
        naomi = [x for x in n]
        ken = [x for x in k]

    start()
    #print (naomi)
    #print (ken)
    naomi.reverse()
    ken.reverse()
    
    while len(naomi) > 0:
        if naomi[0] > ken [0]:
            ken.remove(ken[len(ken)-1])
            fairwin += 1
        else: ken.remove(ken[0])
        naomi.remove(naomi[0])

    start()
    index = 0

    def deceit (na, ke):
        global deceitwin
        for i in range(len(na)):
            for j in range(len(ke)):
                if na[i] > ke [j]:
                    na.remove(na[i])
                    ke.remove(ke[j])
                    deceitwin += 1
                    return na, ke
                if na[i] < ke[j]:
                    break
        return [], []
                
    while len(naomi) != 0:
        naomi, ken = deceit(naomi, ken)
        #print (naomi, ken)

    print ('Case #', end = '', file = fout)
    print (a+1, end = '',file = fout)
    print (':',deceitwin, fairwin,file = fout)
    #print (deceitwin,fairwin)
fout.close()
