fand=open('A-small-attempt0.in')
for line in fand:
    line=line.strip()
    test_case=int(line)
    break
f2=open('Output.txt',"w")
ol=0
for _ in xrange(test_case):
    for line in fand:
        ol+=1
        line=line.strip()
        b=map(int,line[2:])
        needed=0
        #print line[0]
        if(b[0]==0):
            needed=1
            b[0]=1
        standing=b[0]
        i=1
        #for i in xrange(1,(int(line[0])+1)):
        while(True):
            if(standing>=int(line[0])):
                break
            else:
                try:
                    while((standing>=i and b[i]!=0)):
                        standing+=b[i]
                        i+=1
                    if(standing<i and b[i]!=0):
                        needed+=i-standing
                        standing+=i-standing+b[i]
                        i+=1
                    else:
                        i+=1
                except:
                    break
        print 'Case #%s:'%(ol),needed
        f2.write('Case #%s: %s\n'%(ol,needed))
f2.close()
