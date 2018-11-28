d={}
d['z']='q'
d['q']='z'
s1='ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
s2='our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'
for i in range(len(s1)):
    d[s1[i]]=s2[i]
inp=input()
f=open(inp)
a = f.read()
f.close()
a=a.split('\n')[1:]
gans = ''
for i in range(len(a)):
    ans = ''
    for j in a[i]:
        ans+=d[j]
    gans += 'Case #'+str(i+1)+': '+ans+'\n'
f=open('a.out', 'w')
f.write(gans)
f.close()
