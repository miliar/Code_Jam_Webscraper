#!/usr/bin/python


def convert(x):
    print x
    p = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv yeqz'.index(x)
    return 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up aozq'[p]

fin = open('googlerese.in')
T = int(fin.readline())
fout = open('googlerese.out','w')
for i in range(T):
    fout.write('Case #'+str(i+1)+': '+''.join([convert(x) for x in fin.readline().strip()])+'\n')
fout.close()
fin.close()
