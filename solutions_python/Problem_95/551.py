

def process(filein,fileout):

    f_in=open(filein).read().split('\n')
    f_out=open(fileout,'w')

    n=int(f_in[0])

    for i in range(n):
        t=f_in[1+i]
        ans=solve1(t)
        f_out.write("Case #%d: %s\n" % (1+i,ans))
    f_out.close()


def solve1(t):
    trans={'z':'q','q':'z'}
    for (a,b) in zip("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv",
                     "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"):
        trans[a]=b

    ans=''
    for c in t:
        if c in trans:
            ans+=trans[c]
        else:
            ans+='?'

    return ans


process("1small.txt","1small_out.txt")

