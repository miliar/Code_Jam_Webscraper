def normal(nao,ken):
    nao1=[]
    ken1=[]
    nao1=nao[0:]
    ken1=ken[0:]
    #print "hi"    
    nao1.sort()
    ken1.sort()
    nao1.reverse()
    #ken.reverse()
    
    nao_win=0
    while ken1!=[] and nao1!=[]:
        count=0
        found=0
        for e in ken1:
            if e>nao1[0]:
                found=1                
                break
            count=count+1
            
        if found:
            nao1.pop(0)
            ken1.pop(count)
        else:
            nao1.pop(0)
            ken1.pop(0)
            nao_win+=1
    return str(nao_win)            
            
            
def dec(nao,ken):
    nao.sort()
    ken.sort()
    nao.reverse()
    ken.reverse()
    nao_win=0
    
    while ken!=[] and nao!=[]:
       
        if nao[0]>ken[0]:
            nao.pop(0)
            ken.pop(0)
            nao_win+=1
        else:
            nao.pop(-1)
            ken.pop(0)
            
    return str(nao_win)          
    

file=open("c:/users/rhv/Desktop/code_jam/2014/D-large.in","r")
file1=open("c:/users/rhv/Desktop/code_jam/2014/deceit_out_large.txt","w")
m=file.readline()
i=0
l = m.split()


while i<int(l[0]):
    k=[]
    m1=file.readline()
    m2=m1.split()
    blocks = int(m2[0])
    nao=[]
    ken=[]

    #Naomi
    j=0
    m3=file.readline()
    m4=m3.split()
    while j<blocks:
        temp=float(m4[j])
        nao.append(temp)
        j=j+1
    #Ken
    j=0
    m5=file.readline()
    m6=m5.split()
    while j<blocks:
        temp=float(m6[j])
        ken.append(temp)
        j=j+1
    
    ans = normal(nao,ken)
    ans1=dec(nao,ken)
    
    d = "Case #" + str(i+1) +": "+ans1+" "+ans+"\n"
    file1.write(d)
    i=i+1

file.close()
file1.close()
