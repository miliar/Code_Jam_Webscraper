
def min_flips(l, k, flips_count):
    if flips_count > len(l):
        return -1
    ret = ''
    if (l.count('-')):
        cnt = 0
        for i, p in enumerate(list(l)):
            if (cnt == 0 and p == '-' and i + k <= len(l)) or (cnt > 0 and cnt < k):
                if cnt == 0:
                    flips_count += 1
                p = flip(p)
                cnt += 1
            
            ret += p
        if (ret == l):
            return -1
        else:
            return min_flips(ret, k, flips_count)
    else:
        return flips_count
            

def flip(p):
    if (p == '-'):
        return '+'
    else:
        return '-'                

with open('flipper_sm.in','r') as fin, open('flipper_sm.out','w') as fout:
    for i, l in enumerate(fin):
        if (i > 0):
            input_vars = l.split()
            flips_count = min_flips(input_vars[0], int(input_vars[1]), 0)
            fout.write('Case #%d: %s\n' % (i, flips_count if flips_count > -1 else 'IMPOSSIBLE'))