# maps encoded to decoded
d = {'y' : 'a', 'o' : 'e', 'z' : 'q', ' ' : ' ', '\n' : ''}

def decode(enc):
    return "".join(d[c] for c in enc)

def train(d, dec, enc):
    for (a,b) in zip(dec, enc):
        d[b] = a

def trainRemaining(d):
    missingEnc = ' '
    missingDec = ' '
    keys = set(d.keys())
    vals = set(d.values())
    for i in xrange(ord('a'), ord('z')+1):
        if chr(i) not in keys:
            missingEnc = chr(i)
        if chr(i) not in vals:
            missingDec = chr(i)
    d[missingEnc] = missingDec

def solve(fil):
    lNum = 0
    with open(fil) as f:
        for line in f:
            pass
            if lNum > 0:
                print "Case #%d: %s" % (lNum, decode(line))
            lNum += 1

train(d, "our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi")
train(d, "there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
train(d, "so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv")
trainRemaining(d)
