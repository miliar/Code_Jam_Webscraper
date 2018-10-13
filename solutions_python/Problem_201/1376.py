import math

with open('C-small-2-attempt1.in') as f:
#with open('input.in') as f:
    f.readline()
    casecount = 1
    for l in f:
        casestr = 'Case #{}:'.format(casecount)
        casecount += 1
        n = int(l.split()[0])
        k = int(l.split()[1])
        depth = int(math.floor(math.log(k,2)))
        curdepth = [n]
        for i in range(depth):
            #print curdepth
            nextdepth = []
            for x in curdepth:
                nextdepth.append(int(math.floor((x-1)/2.)))
                nextdepth.append(int(math.ceil((x-1)/2.)))
            curdepth = nextdepth
        curdepth.sort(reverse=True)
        x = curdepth[k - ((2**depth) - 1) -1]
        ma = int(math.ceil((x-1)/2.))
        mi = int(math.floor((x-1)/2.))
        print '{} {} {}'.format(casestr, ma, mi)
