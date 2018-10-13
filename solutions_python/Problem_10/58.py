import sys

def read_file(file_name):
    lines = []
    for line in open(file_name):
        lines.append(line.strip())
    lines.reverse()
    cases = int(lines.pop())
    while lines:
        p, k, l = lines.pop().split()
        p = int(p)
        k = int(k)
        l = int(l)
        f = lines.pop().split()
        f = [int(i) for i in f]
        yield p, k, l, f

def small(p, k, f):
    f.sort()
    f.reverse()
    press = 0
    count = 0
    mul = 1
    for i in xrange(0, len(f)):
        if count == k:
            mul += 1
            count = 0
        press += (mul*f[i])
        count += 1

    return press

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    wfile = open(out_file, 'w')
    case_no = 0
    for p, k, l, f in read_file(in_file):
        if p*k < l:
            res = 'Impossible'
        else:
            res = small(p, k, f)
        case_no += 1
        wfile.write('Case #'+str(case_no)+': '+str(res)+'\n')
    wfile.close()



#END