

f=open("B-large.in.txt","r")
lines=f.readlines()
f.close()

resultats=[]
N=eval(lines[0])

for i in range(1,N+1):
    print("case #"+str(i))
    combine={}
    oppose=[]
    

    l=lines[i].split()

    temp=0
    n_c=eval(l[0])

    for j in range(n_c):
        temp=temp+1
        s=l[temp]
        s1=s[:2]
        s2=s[2:]
        combine[s1]=s2
        combine[s1[1]+s1[0]]=s2

    temp=temp+1

    
    n_o=eval(l[temp])

    for j in range(n_o):
        temp=temp+1
        oppose.append(l[temp])
        oppose.append(l[temp][1]+l[temp][0])

    seq=l[temp+2:]
    seq=seq[0]
    length=len(seq)
    
    stri=''
    for j in range(length):        
        stri=stri+seq[j]
        #print(stri)
        

        if len(stri)>=2:
            compare=stri[len(stri)-1]+stri[len(stri)-2]
            if compare in combine:
                stri=stri[:len(stri)-2]+combine[compare]

            for k in range(len(stri)):
                for h in range(k+1,len(stri)):
                    group=stri[k]+stri[h]
                    if group in oppose:
                        stri=''
                
    resultats.append(stri)
    



for i in range(len(resultats)):
    word=resultats[i]
    temp=[]
    length=len(word)

    temp="Case #"+str(i+1)+": ["

    for j in range(length-1):
        temp=temp+word[j]+", "

    if len(word)>0:   
        temp=temp+word[-1]

    temp=temp+"]\n"

    resultats[i]=temp

f=open("o.in","w")
f.writelines(resultats)
f.close()

    
            
        

    
