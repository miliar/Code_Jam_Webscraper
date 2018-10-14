fin = open("D-large.in", 'r')
#fin = open("test.txt", 'r')
fout= open("out.txt", 'w')




testCaNum= int(fin.readline().strip())
for testCa in range(1, testCaNum +1):
    num = int(fin.readline().strip())
    nlog = fin.readline().strip().split()
    klog = fin.readline().strip().split()
    
    dpoint = 0
    wpoint = 0
    for i in range(len(klog)):
        nlog[i] = float(nlog[i])
        klog[i] = float(klog[i])
    nlog.sort()
    klog.sort()
    klog1 = []+klog
    #normal war
    for i in nlog:
        w = 0
        for j in range(len(klog)):
            if i < klog[j]:
                w = 1
                klog.pop(j)
                break
            
        if w == 0:
            klog.pop(0)
            wpoint = wpoint + 1
    #d war
    for i in nlog:
        w = 0
        if i < klog1[0]:
            
            klog1.pop(len(klog1)-1)
        else:
            klog1.pop(0)
            dpoint = dpoint + 1    
            
        
    
    
    fout.write("Case #"+str(testCa)+": "+ str(dpoint)+" "+str(wpoint)+"\n")
        
fin.close()
fout.close()
