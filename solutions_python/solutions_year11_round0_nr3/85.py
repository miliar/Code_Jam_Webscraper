## QUESTION 3

def calc_3(lst):
    xor_all = 0
    for l in lst:
        xor_all ^= l
    if xor_all == 0:
        return str(sum(lst) - min(lst))
    else:
        return 'NO'

def solve(filename, out_file):
    lines = [x[:-1] for x in open(filename).readlines()]
    out = open(out_file, 'a')
    times = int(lines[0])
    for i in range(1, times + 1):
        out.writelines('Case #%d: %s\n' % (i, calc_3([int(x) for x in lines[2*i].split(' ')])))
