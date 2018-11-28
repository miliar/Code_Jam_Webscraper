result=[]
#with open('a.txt','r') as f:
#        for line in f:
##            result.append(map(float,line.split(',')))
#            result.append(line.split(' ')[:-1])    
#print(result)
a=[[],[],[],[]]
with open('aa.txt','r') as f:
    n = int(f.readline())
    for i in range(n):
        
        a[0] = f.readline()
        a[1] = f.readline()
        a[2] = f.readline()
        a[3] = f.readline()
        b = f.readline()
        
        flag = 0
        draw = 1
        for j in range(4):
            if(flag==0):
                x=0
                t=0
                o=0
                for k in range(4):
                    
                    if(a[j][k]=='X'):
                        x=x+1
                    elif (a[j][k]=='O'):
                        o=o+1
                    elif (a[j][k]=='T'):
                        t=t+1
                    elif (a[j][k]=='.'):
                        draw=0
                
                if(x==4 or (x==3 and t==1)):
                    flag = 1
                    print 'Case #'+str(i+1)+': X won'
                elif(o==4 or (o==3 and t==1)):
                    flag = 1
                    print 'Case #'+str(i+1)+': O won'
                
        for j in range(4):
            if(flag==0):
                x=0
                t=0
                o=0
                for k in range(4):
                    
                    if(a[k][j]=='X'):
                        x=x+1
                    elif (a[k][j]=='O'):
                        o=o+1
                    elif (a[k][j]=='T'):
                        t=t+1
                    elif (a[k][j]=='.'):
                        draw=0
                
                if(x==4 or (x==3 and t==1)):
                    flag = 1
                    print 'Case #'+str(i+1)+': X won'
                elif(o==4 or (o==3 and t==1)):
                    flag = 1
                    print 'Case #'+str(i+1)+': O won'
        
        if(flag==0):
            x=0
            t=0
            o=0
            for j in range (4):
#                print a[j][j]
                if(a[j][j]=='X'):
                    x=x+1
                elif (a[j][j]=='O'):
                    o=o+1
                elif (a[j][j]=='T'):
                    t=t+1
                elif (a[j][j]=='.'):
                    draw=0
            if(x==4 or (x==3 and t==1)):
                flag = 1
                print 'Case #'+str(i+1)+': X won'
            elif(o==4 or (o==3 and t==1)):
                flag = 1
                print 'Case #'+str(i+1)+': O won'    
#            print x,o,t
            
        if(flag==0):    
            x=0
            t=0
            o=0
            for j in range (4):
                if(a[3-j][j]=='X'):
                    x=x+1
                elif (a[3-j][j]=='O'):
                    o=o+1
                elif (a[3-j][j]=='T'):
                    t=t+1
                elif (a[3-j][j]=='.'):
                    draw=0
            if(x==4 or (x==3 and t==1)):
                flag = 1
                print 'Case #'+str(i+1)+': X won'
            elif(o==4 or (o==3 and t==1)):
                flag = 1
                print 'Case #'+str(i+1)+': O won'     
#            print x,o,t
        
                     
        if flag == 0 and draw ==1:
            print 'Case #'+str(i+1)+': Draw'
        elif(flag == 0 and draw ==0):
            print 'Case #'+str(i+1)+': Game has not completed'
                
                
                
#        if (a[0]==a[1] and a[1]==a[2]) or (a[1]==a[2] and a[2]==a[3]):
#            flag = 1
#            if a[1]=='X':
#                print 'Case #'+str(i+1)+': X won'
#            else:
#                print 'Case #'+str(i+1)+': O won'
             
        
#        print 'Case #'+str(i)+':' + b