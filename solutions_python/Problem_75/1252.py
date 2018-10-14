from math import *
qwe=1
#f=open("D-small-attempt0.in","r")
f=open("B-small-attempt4.in","r")
fo=open("btst.out","w")
w=int(f.readline()[:-1])
for q in range(0,w):
    tmp=f.readline()[:-1].split(" ")
    dst=tmp[-1]
    tmp=tmp[:-2]
    cmb=[];opp1=[];opp2=[]
    cmbto=[]
    togo=[]
    a=int(tmp[0])
    for i in range(1,a+1):
        cmb.append(tmp[i][:2])
        cmbto.append(tmp[i][2])
        cmb.append(tmp[i][1]+tmp[i][0])
        cmbto.append(tmp[i][2])
        
    b=int(tmp[1+a])
    for i in range(1,b+1):
        opp1.append(tmp[a+i+1][0])
        opp2.append(tmp[a+i+1][1])
        
    #print cmbto,"\n",cmb
    res=""
    for i in dst:
        res+=i
        #print res,"2"

        tre=res[-2:]
        #if(tre in cmb):
        #    #print tre,"tre"
        #    res=res[:-2]+cmbto[cmb.index(tre)]
        #    togo=[]
        #    continue
            
        #for j in range(0,len(togo)):
        #    togo[j][1]+=i
        #    if(togo[j][1][-1]==togo[j][0]):
        #        break
        #    else:
        #        togo[j][1]+=i
        #        #print togo[j][1],"togo1",togo[j][0],togo
        #        if togo[j][1] in res:
        #            res=res[:res.find(togo[j][1])]+res[res.find(togo[j][1])+len(togo[j][1]):]
        #            #togo=[]
        #            #break
        #if(i in opp1):
        #    togo.append([opp2[opp1.index(i)],i])
        #if(i in opp2):
        #    togo.append([opp1[opp2.index(i)],i])
        #print togo,"oo"
    res2=""
    for i in dst:
        res2+=i
        if(res2[-2:] in cmb):
            res2=res2[:-2]+cmbto[cmb.index(res2[-2:])]
            continue
        if(i in opp1):
            if(opp2[opp1.index(i)] in res2):
                res2=""
        if(i in opp2):
            if(opp1[opp2.index(i)] in res2):
                res2=""
    print res,"res",togo,cmb
    print res2,"finally"
    fo.write("Case #%d: ["%(qwe))
    qwe+=1
    for i in res2[:-1]:
        fo.write(i.capitalize()+", ")
    if(len(res2)>0):
        fo.write(res2[-1].capitalize()+"]\n")
    else:
        fo.write("]\n")
f.close()
fo.close()