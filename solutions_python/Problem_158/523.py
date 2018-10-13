t=input()
x=[]
r=[]
c=[]
for i in range(t):
    s=raw_input()
    s=s.split()
    x.append(int(s[0]))
    r.append(int(s[1]))
    c.append(int(s[2]))

def rg(a,b,c):
    if a==1:
        return "GABRIEL"

    elif a==2:
        if (b*c)%2==0:
            return "GABRIEL"
        else:
            return "RICHARD"

    elif a==3:
        if (b*c)%3!=0:
            return "RICHARD"

        else:
            if (b*c)/3==1:
                return "RICHARD"

            else:
                return "GABRIEL"

    elif a==4:
        if (b*c)%4!=0:
            return "RICHARD"

        else:
            if (b*c)/4==1:
                return "RICHARD"

            elif (b*c)/4==2:
                return "RICHARD"

            elif (b*c)/4==3:
                    return "GABRIEL"

            elif (b*c)/4==4:
                    return "GABRIEL"
                
                
for y in range(t):
    print "Case #"+str(y+1)+": "+rg(x[y],r[y],c[y])
            
                

            
            
    
        
        

        
    
