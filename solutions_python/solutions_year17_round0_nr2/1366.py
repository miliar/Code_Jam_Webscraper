for t in xrange(1, input()+1):
    val = list(str(int(raw_input(), 10)))
    
    for idx in xrange(len(val)-2, -1, -1):
        a, b = int(val[idx]), int(val[idx+1])
        if a > b:
            val[idx] = str(a-1)
            for j in xrange(idx+1, len(val)):
                if val[j] == '9': break
                else: val[j] = '9'
        
    while val[0] == '0': val.pop(0)
    res = ''.join(val)
    
    print 'Case #{}: {}'.format(t, res)
