filename = 'B-large'

fin = open(filename + '.in', 'r')
out = open(filename + '.out', 'w')

T = int( fin.readline() )

for t in range(1, T+1):
    line = fin.readline().split(' ')
    C = int(line.pop(0))
    
    combs = {}
    for i in range(0,C):
        cmb = line.pop(0)
        combs[cmb[0:2]] = cmb[2]
        combs[cmb[1::-1]] = cmb[2]
    
    
    
    D = int(line.pop(0))
    
    oposed = {}
    
    for i in range(0, D):
        ops = line.pop(0)
        oposed[ops] = 1
        ops = ops[::-1] # reverse ops
        oposed[ops] = 1

        
    N = int(line.pop(0))
    series = line.pop(0).strip()
    
    # print combs
    # print oposed
    # print series
    # print line
    
    formed = []
    last = ''
    
    for s in series:
        pair = last + s
        cmbn = combs.get(pair)
        if cmbn:
            last = cmbn
            formed[len(formed)-1] = last
            
        else:
            isopposed = False
            # opposed ?
            for fr in formed:
                if oposed.get(fr+s) == 1:
                    last = ''
                    formed = []
                    isopposed = True
                    
            if not isopposed:
                last = s
                formed += [last]
    
    if len(formed) == 0:
        out.write('Case #%d: []\n' % t)
        
    else:
        out.write('Case #%d: [' % t)
        
        fr = formed.pop(0)
        out.write('%s' % fr)
        
        for fr in formed:
            out.write(', %s' % fr)
            
        out.write(']\n')
