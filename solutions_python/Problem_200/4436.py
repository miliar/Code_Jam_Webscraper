from sys import stdin
def numbers():
    n=int(stdin.readline().strip())
    c=0
    while n>0:
        c+=1
        a=stdin.readline().strip()
        mini=int(a[0])
        tau=False
        rest=str()
        same=[]
        possame='NULL'
        if len(a)==1:
            print('Case #'+str(c)+': '+str(a))
        else:
            for x in range(len(a)):
                    
                    if int(a[x])>mini and not tau:
                        mini=int(a[x])
                        same=[]
                    elif int(a[x])==(mini) and not tau:
                        same.append(a[x])
                        possame=x
                        
                    else:
                        if not tau:
                            
                            if a[possame]==a[possame-1] and a[possame]!=a[possame-2] and possame-2>=0:
                                
                                for i in same:
                                    rest+=i
                            if len(same)>=2:
                                
                            
                                for i in same:
                                    rest+=i
                            tau=True
                    if tau:
                        
                        rest+=str(a[x])
                        
            rest=str(rest)
            leng=len(a)-len(rest)-1
            
            if rest!=str():
                
                rest=int(rest)+1
            else:
                rest=0
            rest=str(rest)
            result=int(a)-int(rest)
            if result==-1:
                rest=list(rest)
                rest.pop(0)
                rest="".join(rest)
                result=int(a)-int(rest)
                
            
        
            
            print('Case #'+str(c)+': '+str(result))
            

        n-=1
numbers()
