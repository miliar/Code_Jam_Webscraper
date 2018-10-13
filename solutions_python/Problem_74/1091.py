def go():
    f=open(r"C:\Users\bokajima\Desktop\1.txt")
    cases=int(f.readline())
    for c in range(cases):
        buttons=f.readline().split()[1:]
        order=[]
        olist=[]
        blist=[]
        x=0
        while x<len(buttons):
            if buttons[x]=='O':
                olist.append(int(buttons[x+1]))
                order.append('o')
            else:
                blist.append(int(buttons[x+1]))
                order.append('b')
            x+=2
        opos=1
        bpos=1
        t=0
       
        while olist or blist:
            opushed=0
            if olist and opos<olist[0]:
                opos+=1
            elif olist and opos>olist[0]:
                opos-=1
            elif olist and opos==olist[0] and order[0]=='o':
                del order[0]
                del olist[0]
                opushed=1
                
            if blist and bpos<blist[0]:
                bpos+=1
            elif blist and bpos>blist[0]:
                bpos-=1
            elif blist and bpos==blist[0] and order[0]=='b' and not opushed:
                del order[0]
                del blist[0]
            t+=1

        print 'Case #%s: %d'%(c+1,t)
    f.close()
        
            
        
        
        
