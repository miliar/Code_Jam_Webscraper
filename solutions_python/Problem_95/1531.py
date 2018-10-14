s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq'
s2 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz'

ls = {}
for i in range(len(s1)):
    ls[s1[i]] = s2[i]
f = open("A-small-attempt0.in", 'r')
f1 = open("tongues.out", 'w')
num = int(f.readline())
count = 0
for i in f:
    i = i.rstrip('\n')
    count+=1
    ans = ''
    for n in range(len(i)):
        ans += ls[i[n]]
    f1.write("Case #"+str(count)+": "+ans+"\n")
    
