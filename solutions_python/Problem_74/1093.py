T=int(input())
for n in xrange(T):
    seq = str(raw_input())
    seq = seq.split()
    turn,orange,black =[],[],[]
    x=1
# Index, current postion in list , Button Number
    o=[0,1]
    b=[0,1]
    t,cc=0,0
    flag=0
    while (x <(len(seq))):
        turn.append((seq[x] ,int( seq[x+1])))
        if( seq[x]=='O'):
            orange.append((seq[x] , int(seq[x+1])))
        else:
            black.append((seq[x] , int(seq[x+1])))
        x+=2
    for x in turn:
        if( x[0] == 'O'):
            cc+=abs( x[1] - o[1]) +1
            t=abs( x[1] - o[1])
            o[1]=x[1]
            if(b[0]<len(black)):
                #print b,black[b[0]]
                temp = (b[1] - black[b[0]][1])
                #print "temp" ,temp,t
                if( temp ==0):
                    pass
                else:
                    if( abs( temp)<= t):
                        #print "dasfasdfas"
                        b[1]= black[b[0]][1]
                    else:
                        flag=1
                        if( temp>0):
                            b[1]-= max(1,t)
                        else:
                            b[1]+= max(1,t)

            if(flag==1 and t!=0):
                if(temp>0):
                    b[1]-= 1
                else:
                    b[1]+= max(1,1)
            o[0]+=1
        else:
            cc+=abs( x[1] - b[1]) +1
            t=abs( x[1] - b[1])
            b[1]=x[1]
            if(o[0]<len(orange)):
                temp = (o[1] - orange[o[0]][1])
                if( temp ==0):
                    pass
                else:
                    if( abs( temp)<=t):
                        o[1]= orange[o[0]][1]
                    else:
                        flag=1
                        if( temp>0):
                            o[1]-= max(1,t)
                        else:
                            o[1]+= max(1,t)
            if(flag==1 and t!=0):
               if(temp>0):
                   o[1]-= max(1,1)
               else:
                   o[1]+= max(1,1)
            b[0]+=1
        #print flag
        flag=0
        #print t,o,b
        #print t
    print "Case #%d: %d"%(n+1,cc)
    #print t,b,len(b),o,len(o)
