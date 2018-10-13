import sys

for _ in range(int(sys.stdin.readline())):
    l=sys.stdin.readline().strip().split(" ")
    o=1
    b=1
    m=0
    mb=0
    mo=0
    c=0
    a=int(l[0])
    while a>c:
        if (l[c*2+1]=="O"):
            if mo>0 :
                x=min(abs(int(l[c*2+2])-o),mo)
                mo-=x
                if int(l[c*2+2])<o:
                    o-=x
                else:
                    o+=x
            mb+=1
        else:
            if mb>0 :
                x=min(abs(int(l[c*2+2])-b),mb)
                mb-=x
                if int(l[c*2+2])<b:
                    b-=x
                else:
                    b+=x
            mo+=1
        if (l[c*2+1]=="O"):
            mo+=1
        else :
            mb+=1
        if (l[c*2+1]=="O" and o==int(l[c*2+2])) or (l[c*2+1]=="B" and b==int(l[c*2+2])):
            if (l[c*2+1]=="O"):
                mo=0
            else :
                mb=0
            c+=1
        m+=1
    print("Case #"+str(_+1)+": "+str(m))
      
        
        
