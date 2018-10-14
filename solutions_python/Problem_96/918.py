def test(score, target):
    if not score and target:
        return False, False
    mean = score/3
    mod = score%3
    if mod:
        mean += 1
    if mod == 1:
        return mean >= target, mean >= target
    return mean >= target, (mean + 1) >= target
    
def process(scores, target, S):
    normal = 0
    surprising = 0
    #print 'Scores: %s, Target: %s'%(scores, target)
    for score in scores:
        n, s = test(score, target)
        if n:
            #print '  %s is normal'%score
            normal += 1
        elif s:
            #print '  %s is surprising'%score
            surprising += 1
    #print '  total %s normal and %s surprising (max %s)'%(normal, surprising, S)
    if S <= surprising:
        surprising = S
    #print '  returning %s'%(normal+surprising)
    return normal + surprising

def run(inpath, outpath):
    fin = open(inpath, 'rU')
    fout = open(outpath, 'w')

    for i, line in enumerate(fin):
        if not i:
            continue
        #print 'Line: %s'%line.strip()
        _, S, p, nums = line.strip().split(' ', 3)
        lst = [int(n) for n in nums.split()]
        val = process(lst, int(p), int(S))
        print 'Case #{0}: {1}'.format(i, val)
        fout.write('Case #{0}: {1}\n'.format(i, val))
        #print

    fin.close()
    fout.close()
