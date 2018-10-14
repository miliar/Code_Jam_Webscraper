import itertools

#casename = 'sample'
#casename = 'small'
casename = 'large'

def solve():
    fi = open('magicka_'+casename+'_in.txt','r')
    fo = open('magicka_'+casename+'_out.txt','w')
    T = int(fi.readline())
    for t in xrange(1,T+1):
        parts = fi.readline().split()
        C = int(parts[0])
        combines = parts[1:C+1]
        D = int(parts[1+C])
        opposed = parts[2+C:2+C+D]
        toinvoke = parts[-1]

        lst = []

        for base in toinvoke:
            lst.append(base)
            changed = True
            while changed:
                changed = False
                for cmb in combines:
                    if len(lst)>1:
                        if (((lst[-1]==cmb[0]) and (lst[-2]==cmb[1])) or
                           ((lst[-2]==cmb[0]) and (lst[-1]==cmb[1]))):
                           lst = lst[:-2] + [cmb[2]]
                           changed = True
            for ops in opposed:
                if (ops[0] in lst) and (ops[1] in lst):
                    lst = []
                    
        fo.write("Case #%d: %s\n"%(t,'['+', '.join(lst)+']'))
    fi.close()
    fo.close()
        
