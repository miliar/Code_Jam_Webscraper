def get_content(path):
    return [line.strip() for line in open(path, 'rb')]

    
totals = {}
    
    
def mem_calc(i, j, k):
    if (i, j) not in totals:
        val = i & j
        totals[(i, j)] = val
    else:
        val = totals[(i, j)]
    if val < k:
        return (i, j)
    
    
def calc(content):
    cases = content.pop(0)
    ret = []
    for case in xrange(int(cases)):
        opts = []
        a, b, k = [int(x) for x in content.pop(0).split()]
        for i in xrange(a):
            for j in xrange(b):
                memval = mem_calc(i, j, k)
                if memval:
                    opts.append(memval)
                
        
        ret.append('Case #{}: {}'.format(case + 1, len(set(opts))))
        print "case {}".format(case + 1)
    return ret
    
if __name__ == '__main__':
    content = get_content(r'C:\gjam\1B\2\B-small-attempt2.in')
    ret = calc(content)
    with open(r'C:\gjam\1B\2\out.txt', 'wb') as fwriter:
        for line in ret:
            fwriter.write(line)
            fwriter.write('\r\n')
