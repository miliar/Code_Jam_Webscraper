dic={}
s2='our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
s1='ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
for i in range(len(s1)):
    dic[s1[i]]=s2[i]
dic['q']='z'
dic['z']='q'
##tmp='ejp mysljylc kd kxveddknmc re jsicpdrysi'
##tmp2=''
##for i in tmp:
##    tmp2+=dic[i]
##print tmp2
f=open('A-small-attempt2.in','r')
n=int(f.readline())
for i in range(n):
    tmp=f.readline()
    tmp2=''
    print 'Case #'+str(i+1)+':',
    for i in tmp:
        if i!='\n':
            tmp2+=dic[i]
    print tmp2
        
    

    
