# -*- coding: utf-8 -*-

def get_binary_str(n, s=''):
    s = '%d%s' % (n%2, s)
    n /= int(2)
    if n > 0:
        return get_binary_str(n, s)
    else:
        return s

if __name__=="__main__":
    import time
    start = time.time()
    cnt = 1
    out = open('A-large.out', 'w')
    for l in open('A-large.in'):
        data = l.rstrip("\n").split(' ')
        if len(data) != 2:
            continue
        status = get_binary_str(int(data[1]))
        num_snapper = int(data[0])
        if len(status) > num_snapper:
            r = status[len(status)-num_snapper:]
        elif len(status) == num_snapper:
            r = status
        else:
            r = '0'
            
        if '0' in r:
            out.write('Case #%d: OFF\n' % (cnt))
        else:
            out.write('Case #%d: ON\n' % (cnt))
        cnt += 1
    out.close()

    end = time.time()
    print 'time = %f' % (end - start)
    
