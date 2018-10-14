#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import collections

fi = open("/sdcard/qpython/scripts/C-small-2-attempt1.in","r")
fo = open("/sdcard/qpython/scripts/output","w")

num = int(fi.readline())

for i in range(num):
    inst = fi.readline().split()
    n = int(inst[0])
    k = int(inst[1])

    cnt = collections.Counter()
    cnt[n] = 1
    maxele = n
    maxocc = 1

    while k>1:
        shot = min(k-1,maxocc)
        cnt[(maxele-1)/2] += shot
        cnt[maxele/2] += shot
        cnt[maxele] -= shot
        k -= shot
        maxele = max(cnt.elements())
        maxocc = cnt[maxele]
    
    fo.write("Case #"+str(i+1)+": "+str(maxele/2)+" "+str((maxele-1)/2)+"\n")
    print i
fo.close()
fi.close()