f=open("/home/baralnischal/Downloads/A-small-attempt0.in",'r')
g=open("/home/baralnischal/Downloads/ouptput.txt","w")
t=int(f.readline())

for i in range(t):
    v1=int(f.readline())
    for j in range(1,5):
        new1=f.readline()
        if j==v1:
            a1=new1.split()
    v2=int(f.readline())
    for k in range(1,5):
        new2=f.readline()
        if k==v2:
            a2=new2.split()
    match=[]
    for l in a1:
        for m in a2:
        	if l==m:
        		match.append(l)
    if len(match)==0:
        g.write("Case #"+str(i+1)+": "+"Volunteer cheated!"+'\n')
    elif len(match) ==1:
        g.write("Case #"+str(i+1)+": "+match[0]+'\n')
    else:
        g.write("Case #"+str(i+1)+": "+"Bad magician!"+'\n')
