import sys
import string

# Arguments: [in] [out]
# Defaults: in='input.txt', out=stdout

sample_G = 'qzejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
sample_N = 'zqour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'

# missing G letters: q, z
# missing N letters: q, z
# the hint is 'z' -> 'q'

all = 'abcdefghijklmnopqrstuvwxyz '
def unknown(sample):
    unknown = list(all)
    for c in sample:
        if c in unknown:
            unknown.remove(c)
    for c in unknown:
        print c

#unknown(sample_G)
#unknown(sample_N)

# From Googlerese to Normal
tr = {}

def build_tr():
    for i in range(0,len(sample_G)):
        tr[sample_G[i]] = sample_N[i]
        
def translate(s):
    r = []
    for c in list(s):
        r.append(tr[c])
    return ''.join(r)

build_tr()

if len(sys.argv) > 1:
    input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
    outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
    with open(input_file) as f:
        T = int(f.readline())
        for x in range(T):
            G = f.readline().strip()
            N = translate(G)
            outf.write('Case #{0}: '.format(x+1))
            outf.write(N)
            outf.write('\n')
