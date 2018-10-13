sample=[]
sample.append(("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand"))
sample.append(("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"))
sample.append(("de kr kd eoya kw aej tysr re ujdr lkgc jvzq","so it is okay if you want to just give upqz"))
code = {}
for (e,v) in sample:
    if len(e) != len(v):
        raise Exception("need equal yo!")
    for i in range(len(e)):
        code[ e[i] ] = v[i]
T = int(input())
for tc in range(1,T+1):
    inp = input()
    out = []
    for c in inp:
        out.append( code[c])
    #print("Case #{}: {}".format(tc).format("".join(out)))
    print("Case #{}: {}".format(tc,"".join(out)))
