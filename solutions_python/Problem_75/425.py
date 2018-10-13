import sys

filename='samp.txt'
if len(sys.argv) > 1:
    filename = sys.argv[-1]
    
data = [line.strip().split() for line in open(filename,'r').readlines()[1:]]

for num,case in enumerate(data):
    #R -> Replacements
    #C -> Clear
    #S -> String
    mode = -1
    info = [[],[],[]]
    for val in case:
        if val.isdigit():
            mode+=1
        else:
            info[mode].append(val)
    [R,C,S] = info
    S=S[0]
    R = dict( [ ("".join(sorted(x[:2])),x[2]) for x in R] )
    
    r_val = ''
    for s in S:
        r_val+=s
        lastpair="".join(sorted(r_val[-2:]))
        if R.has_key(lastpair):
            r_val = r_val[:-2]
            r_val += R[lastpair]
        for c in C:
            if c[0] in r_val and c[1] in r_val:
                r_val = ""
    
#    r_val = S
    print "Case #%d: [%s]"%(num+1,", ".join(list(r_val)))


