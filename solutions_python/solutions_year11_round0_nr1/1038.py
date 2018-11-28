f = open('A-large.in','r')
lines=f.readlines()
T = int(lines[0] )
for i in range(1,T+1):
        line=lines[i]
        #print(line)
        tmpLine=[x for x in line.split()]
        #print(tmpLine)
        n=int(tmpLine[0])
        l=[x for x in line[len(tmpLine[0])+1:].split()]
        #print(l)
        sec=0
        Onow=1
        Bnow=1
        tmp=0
        Otmp=0
        Btmp=0
        #print(n)
        #print("======================\n",Onow,Bnow)
        for j in range(0,n):
                turn=l[2*j]
                num=int(l[2*j+1])
                if(turn=='O'):
                        now=Onow
                        Onow=num
                        tmp=Otmp
                        Otmp=0
                else:
                        now=Bnow
                        Bnow=num
                        tmp=Btmp
                        Btmp=0
                if(now > num):
                        if(now-num > tmp):
                                tmp=now-num-tmp+1
                        else:
                                tmp=1
                elif (now < num):
                        if(num-now > tmp):
                                tmp=num-now-tmp+1
                        else:
                                tmp=1
                else:
                        tmp=1
                #print(tmp)
                if(turn=='O'):
                        Btmp+=tmp
                else:
                        Otmp+=tmp
                sec+=tmp
                #print(Onow,Bnow)
        print("Case #%d: %d" % (i,sec))
