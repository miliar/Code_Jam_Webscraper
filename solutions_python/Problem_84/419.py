f = open('a.in')
cases = int(f.readline())
case = 1
while case<=cases:
    s=f.readline()
    r,c = map(int, s.split(' '))
    
    rc = 1
    task=[]
    while rc<=r:
        s = f.readline()
        s=s.rstrip()
        task.append(s)
        rc += 1
    
    i = 0
    j = 0
    impossible = False
    while i<r:
        
        while j<c:            
            if task[i][j]=='#':
                task[i]=task[i][:j]+'/'+task[i][j+1:]
                #task[i][j] = '/'                
                if j+1<c:
                    if (task[i][j+1]=='#'):
                        task[i]=task[i][:j+1]+'\\'+task[i][j+2:]
                        if i+1<r:
                            if (task[i+1][j+1]=='#'):
                                task[i+1]=task[i+1][:j+1]+'/'+task[i+1][j+2:]
                                #task[i+1][j+1] = '/'                                      
                            else:
                                impossible = True                 
                        else:
                            impossible = True                        
                    else:
                        impossible = True                                            
                else:
                    impossible = True

                if i+1<r:
                    if (task[i+1][j]=='#'):
                        task[i+1]=task[i+1][:j]+'\\'+task[i+1][j+1:]
                    else:
                        impossible = True                                            
                else:
                    impossible = True
                    
                
                j += 1                                            

                    
            j += 1
           
        j = 0
        i += 1
    
    print "Case #"+str(case)+":"
    if impossible:
        print "Impossible"
    else:
        for l in task:
            print l
    case += 1