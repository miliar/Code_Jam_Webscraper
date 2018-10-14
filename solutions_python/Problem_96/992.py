
fin = open("./B-large.in",'r')
fout = open("./outputB.out",'w')

case_num = int(fin.readline())

for i in range(1,case_num+1):
    inline = fin.readline()
    ii = inline.split()

    points_num = int(ii[0])
    supri = int(ii[1])
    p = int(ii[2])

    points=[]
    flags = []
    for j in range(3, points_num+3):
        point = int(ii[j])
        if(point==0 and p!=0):flag=0
        elif((point+2)/3.0>=p):flag=2
        elif((point+4)/3.0>=p):flag=1
        else:flag=0
        points.append(point)
        flags.append(flag)
        j+=1

    ans = 0
    for flag in flags:
        if(flag==2):ans+=1
        if(flag==1):
            if(supri>0):
                ans+=1
                supri-=1

    outline = "Case #"+str(i)+": "+str(ans)+"\n"
    fout.write(outline)

fin.close()
fout.close()
    
