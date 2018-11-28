fi_name="A-large.in"
fo_name="A-large.out"
fi=open(fi_name,'r')
fo=open(fo_name,'w')

def lcd(a,b):
    m=a*b
    while b>0:
        temp=b
        b=a%b
        a=temp
    return a

t= int(fi.readline())
for i in range(t):
    check=True
    line=fi.readline().strip().split()
    n=int(line[0])
    pd=int(line[1])
    pg=int(line[2])
    
    if pg==0 or pg==100:
        if pd==pg:
            check=True
        else:
            check=False
    else: 
        if pd==0 or pd==100:
            check=True
        else:
            d=100/lcd(pd,100)
            if n>=d:
                check=True
            else:
                check=False

    if check==False:
        fo.write("Case #"+str(i+1)+": Broken\n")
    else:
        fo.write("Case #"+str(i+1)+": Possible\n")
fi.close()
fo.close()
            
    