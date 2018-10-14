#coding:utf-8

fr=open("A-large.in","r")

output=""
ans=[]
casenum=0

count=0
for line in fr:
    if count==0:
        casenum=int(line)
    else:
        tmp=line.split()
        Smax=int(tmp[0])
        sumnum=0
        level=0
        tmpans=0
        for a in list(tmp[1]):
            number=int(a)
            lack=level-sumnum
            if lack <= 0:#ok
                sumnum=sumnum+number
            else:
                tmpans=tmpans+lack
                sumnum=sumnum+number+lack
            level=level+1
        ans.append(tmpans)
    count=count+1



for i in range(0,casenum):
    output=output+"Case #"+str(i+1)+": "+str(ans[i])+"\n"

fr.close()


fw=open("out.txt","w")
fw.write(output)
fw.close()