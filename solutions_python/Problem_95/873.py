A="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvy qee"
B="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upa zoo"
p={}

for i in range(len(A)):
    p[A[i]]=B[i]
p['z']='q'    
trans=lambda x:p[x]
    
with open("/Users/hanfei/Downloads/A-small-attempt0.in") as ip:
    with open("./1.output","w") as op:
        case_cnt=ip.readline().strip()
        for i in range(int(case_cnt)):
            inp=ip.readline().strip()
            op.write("Case #%s: "%(i+1)+"".join(map(trans,inp))+"\n")
            print "Case #%s: "%(i+1)+"".join(map(trans,inp))+"\n",
            
            
        
    
