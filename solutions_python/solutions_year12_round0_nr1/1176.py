first='ejp mysljylc kd kxveddknmc re jsicpdrysi'
second='rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
third='de kr kd eoya kw aej tysr re ujdr lkgc jv'

firstc='our language is impossible to understand'
secondc='there are twenty six factorial possibilities'
thirdc='so it is okay if you want to just give up'

dict={}

i=0
for e in first:
    if e not in dict:
        dict[e]=firstc[i]
    i+=1
    
i=0    
for e in second:
    if e not in dict:
        dict[e]=secondc[i]
    i+=1

i=0
for e in third:
    if e not in dict:
        dict[e]=thirdc[i]
    i+=1
dict['\n']='\n'
dict['q']='z'
dict['z']='q'
f=open('A-small-attempt0.in','r')
o=open('output.txt','w')
case=0
for line in f:
    s=''
    if case==0:
        maxlines=line
        case+=1
        continue
    for e in line:
        s=s+dict[e]
    o.write('Case #'+str(case)+': '+s)
    case+=1
   

f.close()
o.close()
