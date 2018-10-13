replace = {'a':'y', 'o':'e', 'z':'q', 'q':'z'}
s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
rs1 = 'our language is impossible to understand'
s2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
rs2 = 'there are twenty six factorial possibilities'
s3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
rs3 = 'so it is okay if you want to just give up'

def addtoreplace(s,rs,replace):
    for i in range(len(s)):
        replace[s[i]]=rs[i]
    return replace

def transform(s):
    t = ''
    for i in s:
        t = t + replace[i]
    return(t)


addtoreplace(s1,rs1,replace)
addtoreplace(s2,rs2,replace)
addtoreplace(s3,rs3,replace)
    
inp = open('A-small-attempt0.in','r')
outp = open('A-small-output.txt','w')

x = int(inp.readline())
i=0
while i<x:
    outp.write('Case #'+str(i+1)+': '+transform((inp.readline()).strip())+'\n')
    i+=1

    
inp.close()
outp.close()


