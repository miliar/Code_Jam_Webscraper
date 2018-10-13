s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz"
s2 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq"
d = dict()
for i in range(len(s1)):
    d[s1[i]] = s2[i]

"""
for k,v in d.iteritems():
    print k,v
"""
fin = open("in", "r")
fout = open("out","w")
cases = int(fin.readline())
for i in range(cases):
    line = fin.readline()
    fout.write("Case #{0}: ".format(i+1))
    for j in range(len(line)):
        if d.has_key(line[j]):
            fout.write(d[line[j]])
        else:
            fout.write(line[j])
fin.close()
fout.close()