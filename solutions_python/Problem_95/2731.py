s1='ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz'
s2='our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq'
d=dict(zip(s1,s2))
t=int(input())
for i in range(t):
    s=input()
    print("Case #%d: "%(i+1),end='')
    for c in s:
        print(d[c],end='')
    print()
    