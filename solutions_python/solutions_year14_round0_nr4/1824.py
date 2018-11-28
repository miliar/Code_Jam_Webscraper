fr = open('D-large.in','r')
fw = open('D-large.out','w')

for i in range(0, int(fr.readline())):
    l = int(fr.readline())
    w = 0
    dw = 0
    n = fr.readline().split(" ")
    k = fr.readline().split(" ")
    for a in range(0,l):
        n[a] = float(n[a])
        k[a] = float(k[a])

    n.sort()
    k.sort()
    k_1 = list(k)
    j=0
    for z in range(0, l):
        while j < len(k_1):
            if(n[z]<k_1[j]):
                del(k_1[j])
                break
            else:
                j = j + 1
        if j >= len(k_1):
            w = len(k_1)
            break

    j=0
    for p in range(0, l):
        if n[p] > k[j]:
            j = j + 1
            dw = dw + 1
            
    fw.write('Case #'+str(i+1)+': '+str(dw)+' '+str(w)+'\n')
    
fr.close()
fw.close()
