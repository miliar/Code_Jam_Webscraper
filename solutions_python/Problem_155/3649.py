f=open('A-small-attempt1.in','r')
##ntc=int(raw_input())
ntc=int(f.readline().split()[0])
tc=[]
for i in range(0,ntc):
    tc.append(f.readline().split())
    ctr=0
    out=0
    for j in range(1,(int(tc[i][0])+1)):
            ctr=ctr+int(tc[i][1][j-1])
            if int(tc[i][1][j]) == 0:
                   pass
                   
            else:
                   if ctr>=j:
                       pass
                   else:
                       out=out+j-ctr
                       ctr=ctr+out
    f1=open('output.out','a')
    print >>f1, 'Case #'+ str(i+1) + ': ' + str(out)
    f1.close()
f.close()
                        
                   
                   
    


