#!/usr/bin/python

def calculate_step(k, ggg):
    total = 0
    last_it = 0
    for i, v in enumerate(ggg):
        if total + v[1] <= k: 
            total += v[1]
            last_i = i
        else:
            break
    return last_i, total

def roller_coaster(r, k, n, gg):
    ggg = [(i,v) for (i,v) in enumerate(gg)]
    index = {}
    value  = []
    j = 0
    while j < r:
        value.append(0)
        if ggg[0][0] in index.keys():
            j0 = index[ggg[0][0]]
            cycle = j - j0
            quant = (r - j)/cycle
            value[-1] += quant * sum(value[j0:])
            j += quant * cycle
            while j < r:
                last_i, total = calculate_step(k, ggg)
                ggg = ggg[last_i+1:] + ggg[:last_i+1]
                value[-1] += total
                j += 1
        else:
            index[ggg[0][0]] = j
            last_i, total = calculate_step(k, ggg)
            ggg = ggg[last_i+1:] + ggg[:last_i+1]
            value[-1] += total
        j += 1
    return sum(value)

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        r, k, n = [int(s) for s in raw_input().split()]
        gg = [int(s) for s in raw_input().split()]
        tmp = roller_coaster(r, k, n, gg)
        print 'Case #%d: %s' % (i+1, tmp)
