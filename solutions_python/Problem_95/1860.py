s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
mp = {'q' : 'z', 'z' : 'q'}                         
for i in range(len(s1)): mp[s1[i]] = s2[i]                           
fin = open("input.txt", "r")
fout = open("output.txt", "w")
n = int(fin.readline())
i = 1
for s in fin.readlines():
    s2 = "" 
    for j in range(len(s)-1):s2 += mp[s[j]]
    print >> fout, "Case #" + str(i) + ": " + s2
    i += 1
