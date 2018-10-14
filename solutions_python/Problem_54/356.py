# -*- coding: utf-8 -*-

def gcd(input):
    input.sort()
    if input[0] == 0:
        return input[len(input)-1]
    elif len(input) == 1:
        return input[0]
    else:
        for i, x in enumerate(input):
            if i == 0:
                continue
            input[i] %= input[0]
        return gcd(input)
        
def get_gcds(list_val):
    diff_vals = []
    if len(list_val) == 2:
        diff_vals = [abs(long(list_val[0]) - long(list_val[1]))]
    else:
        for i, x in enumerate(list_val):
            if i == 0:
                continue
            diff_vals.append(abs(long(list_val[i]) - long(list_val[i-1])))
    T = gcd(diff_vals)
    #print 'T = %d' % T
    N = -1
    for x in list_val:
        if long(x) % T == 0:
            N_tmp = 0
        else:
            N_tmp = (long(x) / T + 1) * T - long(x)
        if N != -1 and N != N_tmp:
            print 'ERROR'
        else:
            N = N_tmp
    return N

if __name__=="__main__":
    import time
    start = time.time()
    
    cnt = 1
    out = open('B-small-attempt0.out', 'w')
    for l in open('B-small-attempt0.in'):
        data = l.rstrip("\n").split(' ')
        if len(data) < 2:
            continue
        out.write('Case #%d: %ld\n' % (cnt, get_gcds(data[1:])))
        cnt += 1
    out.close()

    end = time.time()
    print 'time = %f' % (end - start)
