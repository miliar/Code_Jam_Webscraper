fin = open('input.txt','r')
fout = open('output.txt','w')

N = int(fin.readline())
for i in range(N):
    temp = fin.readline().strip().split(' ')
    C, F, X = float(temp[0]), float(temp[1]), float(temp[2])
    
    n = 0       #number of farms
    ct = 0.0    #current time
    pt = X/2    #projected time
    
    while ((X/(2 + (n+1)*F) + C/(2 + n*F)) < pt):
        ct += C/(2 + n*F)
        n += 1
        pt = X/(2 + n*F)
    
    
    
    fout.write("Case #%d: %.7lf\n"%(i+1, ct+pt))

fin.close()
fout.close()

print "If it were done when 'tis done, then 'twere well It were done quickly"