#coding:utf-8

#D人の客が、それぞれPi枚のパンケーキを持っている
#他の客は何もない
#一分に一枚食べる
#specialtimeは誰も食べない、パンケーキ有りの客からその他の客へパンケーキが移る
#できるだけ早くパンケーキをなくす


#kに展開した時のかかる時間数
simulate=lambda pan,k :sum([int((i-1)/k) for i in pan])+k

fr=open("B-large.in","r")

output=""
ans=[]
casenum=0

count=0
for line in fr:
    if count==0:
        casenum=int(line)
    else:
        if (count%2) == 0:#list
            tmpans=10000
            diners=list(map(int,line.split()))
            for i in range(1,max(diners)+1):
                tmp=simulate(diners,i)
                if tmpans>tmp:
                    tmpans=tmp
            ans.append(tmpans)
    count=count+1


for i in range(0,casenum):
    output=output+"Case #"+str(i+1)+": "+str(ans[i])+"\n"

fr.close()


fw=open("out.txt","w")
fw.write(output)
fw.close()