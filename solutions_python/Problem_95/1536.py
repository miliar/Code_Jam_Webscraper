def mapping():
    d={}
    out='yeq z our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
    inp='aoz q ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
    for i in range(len(out)):
        d[inp[i]]=out[i];
    return d;

def translate(inp, d):
    out=''
    for i in range(len(inp)-1):
        out=out+ d[inp[i]]
    return out

def solve(inp):
    return translate(inp, mapping())

f = open('A-small-attempt2.in', 'r')
n=f.readline()
l=f.readline()
n=1
while l:
    
    print "Case #"+ str(n)+': ', solve(l)
    l=f.readline()
    n=n+1
