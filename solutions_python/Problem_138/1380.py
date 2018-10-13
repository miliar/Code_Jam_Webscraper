def checking_optimal_war(N,naomi,ken):
    c = 0

    while (c<len(ken)):
        if (naomi[c]>ken[c]):
            ken.remove(ken[c])
            c-=1
        c+=1
    return N-len(ken)                

def checking_deceitful_war(N,naomi,ken):
    temp = 0
    c = 0
    if min(ken)>max(naomi):
        return 0
    ken_min = min(ken)
    ken_max = max(ken)
    naomi_min = min(naomi)
    while (c<N):
        if(naomi_min>ken_min):
            ken = ken[1:]
            naomi = naomi[1:]           
            temp+=1
        elif (naomi_min<ken_min):
            ken = ken[:-1]
            naomi = naomi[1:]            
        elif (naomi_min>ken_max):
            return N-c+temp
        if(ken):
            ken_max = max(ken)
            ken_min = min(ken)
            naomi_min = min(naomi)
        c+=1
    return temp
    

def result(Dwar,War,index):
    return "Case #"+str(index)+": "+str(Dwar)+' '+str(War)+"\n"

fin = open("D-large.in","r")
fout = open("Dlarge.txt","w")
n = int(fin.readline())
for i in range (0,n):
    N = int(fin.readline())
    s1 = fin.readline()
    naomi = list(map(float,s1.split()))
    s2 = fin.readline()
    ken = list(map(float,s2.split()))
    naomi.sort()
    ken.sort()
    fout.write(result(checking_deceitful_war(N,naomi,ken),checking_optimal_war(N,naomi,ken),i+1))
fout.close()
















    
    
