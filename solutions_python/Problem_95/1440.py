pctable = {}
cptable = {}

def train(p, c):
    if len(p)!=len(c):
        print "Plain/Ciphertext Lengths not match"
        return
    L = len(p)
    for i in range(L):
        if (p[i]==' ' and c[i]!=' ') or (p[i]!=' ' and c[i]==' '):
            print "Format mismatch @ char %d" % (i+1)
            return
        elif c[i] in cptable.keys() and cptable[c[i]] != p[i]:
            print "Advanced cipher algorithm detected. ABORT! ABORT!"
            return
        else:
            pctable[p[i]] = c[i]
            cptable[c[i]] = p[i]

def encode(p):
    return ''.join([pctable[ch] for ch in p])

def decode(c):
    return ''.join([cptable[ch] for ch in c])

#taken from example cases, three mappings given in problem text
#the q->z mapping is deduced from 25 other mappings
trainplain = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up aozq'
traincipher = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv yeqz'

train(trainplain,traincipher)

T = int(raw_input())

for i in range(T):
    P = raw_input()
    print "Case #%d: %s" % (i+1, decode(P))
