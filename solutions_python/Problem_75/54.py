import string
fin=open("B-large.in",'r')
T = int(fin.readline())
result=[]
outfile=open("output.txt","w")
for case in range(1,T+1):
    line0 = fin.readline()

    line0=line0.split()
    n1=int(line0[0])
    
    merge_list=[]
    oppose_list=[]
    for i in range(1,n1+1):
        merge_list.append(line0[i])
    
    n2=int(line0[n1+1])
    
    for i in range(n1+2,n1+n2+2):
        oppose_list.append(line0[i])
    number=line0[n1+n2+2]
    invoke=line0[n1+n2+3]
    result=""
    for i in invoke:
        if result=="":
            result+=i
        else:
            t=result[-1]
            result+=i
            flag=0
            for h in merge_list:
                if (t==h[0] and i==h[1]) or (t==h[1] and i==h[0]):
                    result=result[:-2]+h[-1]
                    flag=1
                    break
            if flag==0:
                for h in oppose_list:
                    if (i==h[0] and h[1] in result[:-1]) or (i==h[1] and h[0] in result[:-1]):
                        result=""
    
    print result           
    if len(result)==0:
        f_str="[]"
    else:
        f_str="["
        for i in result:
            f_str+=i+", "
        
        f_str=f_str[:-2]+"]"
    f_str="Case #%d: %s \n" % (case,f_str)
    outfile.write(f_str)
outfile.close()            
print "done"        
        
        
