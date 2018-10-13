inn=open("c:/downloads/in.in",'r')
T=int(inn.readline())
m1=[[0 for i in range(4)] for i in range(4)]
m2=[[0 for i in range(4)] for i in range(4)]
l=[0 for i in range(4)]
#T - number of cases
rs=open("c:/downloads/rs.rs",'w')
for i in range(T):
    a1=int(inn.readline())-1 #first answer in 0-3 form
    for j in range(4):
        s=inn.readline()
        ss=s.split()
        for k in range(4):
            m1[j][k]=int(ss[k])
    #at this pt m_jk is a 4*4 matrix representing the first configuration
    a2=int(inn.readline())-1 #2nd ans in 0-3 form
    for j in range(4):
        s=inn.readline()
        ss=s.split()
        for k in range(4):
            m2[j][k]=int(ss[k])
    #at this ptwe're ready to analyze: have both answers and both configurations
    #now basically need to compute the number of coincidences
    #in m1[a1] row and m2[a2]
    num=0
    for e in range(4):
        for f in range(4):
            if m1[a1][e]==m2[a2][f]:
                y=m1[a1][e]
                num=num+1
    #now constructing output
    if num==0:
        rs.write("Case #"+str(i+1)+": "+"Volunteer cheated!\n")
    elif num>1:
        rs.write("Case #"+str(i+1)+": "+"Bad magician!\n")
    else:
        rs.write("Case #"+str(i+1)+": "+str(y)+'\n')
inn.close()
rs.close()
