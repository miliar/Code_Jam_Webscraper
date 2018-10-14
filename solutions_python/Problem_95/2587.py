hashtab={}
strings=[]
answers=[]
strings.append("our language is impossible to understand")
strings.append("there are twenty six factorial possibilities")
strings.append("so it is okay if you want to just give up")
answers.append("ejp mysljylc kd kxveddknmc re jsicpdrysi")
answers.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
answers.append("de kr kd eoya kw aej tysr re ujdr lkgc jv")
for j in range(len(strings)):
    for k in range(len(strings[j])):
        hashtab[answers[j][k]]=strings[j][k]
hashtab['q']='z'
hashtab['z']='q'
hashtab['\n']='\n'
a=hashtab.keys()
a.sort()
#for key in a:
#    print(key+":"+hashtab[key])
f=open("A-small-attempt3.in")
lines=f.readlines()
t=int(lines[0])
for i in range(1,t+1):
    line="Case #"+str(i)+": "
    for k in lines[i]:
        if k=='\n':
            continue
        line=line+hashtab[k]
    print(line)
