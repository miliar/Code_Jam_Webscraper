s1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
s2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
map={}
for i in range(0,len(s1)):
	map[s1[i:i+1]]=s2[i:i+1]
map['q']='z'
map['z']='q'
fp=open('A-small-attempt0.in','r')
fw=open('A-large.out','w')
N=int(fp.readline())
for i in range(1,N+1):
        s=fp.readline()
        ss=""
        for ii in range(0,len(s)-1):
                ss=ss+map[s[ii:ii+1]]
        fw.write("Case #"+str(i)+": "+ss)
        fw.write('\n')
fw.close()


