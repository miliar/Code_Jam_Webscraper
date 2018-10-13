def min_scalar(x, y):
    x = [int(i) for i in x]
    y = [int(i) for i in y]
    xx = sorted(x)
    yy = sorted(y)
    yy.reverse()
    res = 0
    for i in xrange(0, len(x)):
        res += int(xx[i])*int(yy[i])

    return res

if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    lines = open(in_file).readlines()
    lines = lines[1:]
    wfile = open(out_file, 'w')
    case_no = 0
    while lines:
        case_no += 1
        lines = lines[1:]
        x = lines[0].strip().split()
        y = lines[1].strip().split()
        lines = lines[2:]
        res = min_scalar(x,y)
        wfile.write('Case #'+str(case_no)+': '+str(res)+'\n')

