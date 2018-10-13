f=open('A-small-attempt5.in','r')
ww=open('1st.txt','w+')
line1=int(f.readline())

a=list()
b=list()
r=0


for x in range (0,line1):
    r=r+1
    line2=int(f.readline())
    
    line11=f.readline()
    line12=f.readline()
    line13=f.readline()
    line14=f.readline()
        
    if line2 == 1:
        a=line11.split()
    elif line2 == 2:
        a=line12.split()
    elif line2 == 3:
        a=line13.split()
    elif line2 == 4:
         a=line14.split()

    line3=int(f.readline())
    
    line15=f.readline()
    line16=f.readline()
    line17=f.readline()
    line18=f.readline()
        
    if line3 == 1:
        b=line15.split()
    elif line3 == 2:
        b=line16.split()
    elif line3 == 3:
        b=line17.split()
    elif line3 == 4:
        b=line18.split()
    q=0
    w=0
    for aa in a:
        for bb in  b:
            if aa == bb:
                q=q+1
                w=aa
    g=str(r)
    if q==0:
        ww.writelines("Case #"+g+": Volunteer cheated!"+"\n")
    elif q ==1:
        ww.writelines("Case #"+g+": "+w+"\n")
    else :
        ww.writelines("Case #"+g+": Bad magician!"+"\n")
                     
