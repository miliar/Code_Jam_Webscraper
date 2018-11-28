file=open("B-small-attempt2.in","r")
count=int(file.readline()[:-1])
for k in range (count):
    CFX=file.readline()[:-1].split(" ")
    mintime=float(CFX[2])/2
    '1farm'
    m=0
    x=1
    while(1):
        timen1=0
        timen2=0
        for y in range (1,x+1):
            timen1+=float(CFX[0])/(2+(y-1)*float(CFX[1]))    
            timen2=float(CFX[2])/(2+(y)*float(CFX[1]))
            m=n=timen1+timen2
            if(m<=mintime):
                mintime=m
        if(mintime<n):
            break        
        x+=1
        
    print("Case #"+str(k+1)+": "+str(mintime))
            
