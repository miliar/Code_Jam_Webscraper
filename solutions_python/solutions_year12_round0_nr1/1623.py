
o1="our language is impossible to understand"
o2="there are twenty six factorial possibilities"
o3="so it is okay if you want to just give up"
o4="a zoo"

i1="ejp mysljylc kd kxveddknmc re jsicpdrysi"
i2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
i3="de kr kd eoya kw aej tysr re ujdr lkgc jv"
i4="y qee"

transcode={}
translated=[i1,i2,i3,i4]
original=[o1,o2,o3,o4]

for i in range(4):
    temp=original[i].split()
    temp2=translated[i].split()
    for j in range(len(temp)):
        for k in range(len(temp[j])):
            if temp2[j][k] not in transcode:
                transcode[temp2[j][k]]=temp[j][k]
transcode['z']='q'
   
f=open("A-small-attempt1.in","r")
lines=f.readlines()
f.close()

N=eval(lines[0])

answer=[]

for i in range(N):
    stri="Case #"+str(i+1)+": "
    sentence=lines[i+1]    
    for letter in sentence:
        if letter in transcode:
            stri=stri+transcode[letter]
        else:
            stri=stri+" "    
    stri=stri+"\n"     
    answer.append(stri)
    
    
            
f=open("o.txt","w")
f.writelines(answer)
f.close()

print(transcode)
