fi=open("B-small-attempt1.in",'r')
fo=open("B-small-attempt1.out",'w')

t=int(fi.readline())
for j in range(t):
    s=fi.readline().split()
    c=int(s[0])
    comb=[]
    for i in range(c):
        comb.append(s[1+i])
    d=int(s[c+1])
    op=[]
    for i in range(d):
        op.append(s[c+1+d])
    n=int(s[c+d+2])
    l=list(s[c+d+3])
    
    res=[l[0]]
    for i in range(1,n):
        res.append(l[i])
        if len(res)>1:
            k=0
            while (k<c):
                
                if (not((comb[k][0]==res[-1] and comb[k][1]==res[-2]) or (comb[k][1]==res[-1] and comb[k][0]==res[-2]))):
                    k+=1
                else:
                    break
            if (k<c):
                res.pop()
                res.pop()
                res.append(comb[k][2])
            else:
                k=0
                while (k<d):
                    if ((op[k][1]==res[-1]) or (op[k][0]==res[-1])):
                        if (op[k][1]==res[-1]):
                            find=op[k][0]
                        else:
                            find=op[k][1]
                        if (find in res):
                            res=[]    
                        break
                    else:
                        k+=1
    
    fo.write("Case #"+str(j+1)+": [")
    for k in range(len(res)-1):
        fo.write(res[k]+", ")
    if (len(res)>0):
        fo.write(res[-1]+"]\n")
    else:
        fo.write("]\n")
fi.close()
fo.close()
        


                       