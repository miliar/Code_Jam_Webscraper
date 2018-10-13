
import itertools

def google():
    fil=open('A-small-attempt0.in','r')
    x=fil.readline()
    ia=1
    p = open("rever.in","w")
    while ia<=int(x):
        c=0
        y=fil.readline()
        l1=[]
        lin=y.split()
        for e in lin:
            l1.append(int(e))
        z=fil.readline()
        l2=[]
        lin2=z.split()
        for e in lin2:
            l2.append(float(e))

        lis =[]
        list1=[]
        for outcome in itertools.product(*len(l2)*((0,1,),)):
            i=0
            f=1
            list1.append(outcome)
            while i<len(outcome):
                if outcome[i]==1:
                    c=l2[i]
                    c=1-c
                    f=f*(c)
                else:
                    c=l2[i]
                    f=f*c
                i=i+1
            lis.append(f)


        keystroke = []
        i=0
        key2 = 0
        le=l1[1]-l1[0]
        
        for out in list1:
            key1 = 0
            if 1 not in out:
                key1 = le + 1
            else:
                key1 = le + 1 +l1[1] + 1
            
            
            key2 = key2 + (key1*lis[i])
            i=i+1
        keystroke.append(key2)
        
        for i in range(1,l1[0]+1):
            j=0
            key2=0
            for out in list1:
                
                if 1 not in out[:-i]:
                    key1 = 2*i + le +1
                else:
                    key1 = 2*i +le +1 + l1[1] +1
                
                key2 = key2 + (key1*lis[j])
                j = j + 1
            
            keystroke.append(key2)
        i = 0
        key2 = 0
        for out in list1:
            if le ==0 and 1 not in out:
                key1 = 1
            else:
                key1 = 1 + l1[1] + 1
            
            key2 = key2 + (key1*lis[i])
            i =i + 1
        
        keystroke.append(key2)
        p.write("Case #"+str(ia)+": "+str(min(keystroke))+"\n")
        ia =ia + 1
    p.close()
    fil.close()


google()
            
                
                
                
        


