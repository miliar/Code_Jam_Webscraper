def read_file(file_name):
    lines = []
    for line in open(file_name):
        lines.append(line.strip())
    lines.reverse()
    cases = int(lines.pop())
    while lines:
        t = int(lines.pop())
        na, nb = lines.pop().split()
        na = int(na)
        nb = int(nb)
        count = 0
        a_start = []
        a_end = []
        while count < na:
            s, e = lines.pop().split()
            a_start.append(hhmm2m(s))
            a_end.append(hhmm2m(e, t))
            count += 1
        count = 0
        b_start = []
        b_end = []
        while count < nb:
            s, e = lines.pop().split()
            b_start.append(hhmm2m(s))
            b_end.append(hhmm2m(e, t))
            count += 1

        yield na, nb , a_start, a_end, b_start, b_end

def hhmm2m(hhmm, t=0):
    h,m = hhmm.split(':')
    h = int(h)
    m = int(m)
    return h*60 + m + t

def count_train(na, nb, a_start, a_end, b_start, b_end):
    if na == 0 or nb == 0:
        return na, nb

    na = 0
    nb = 0

    s = None
    e = None
    start = a_start
    start.sort()
    start.reverse()
    end = b_end
    end.sort()
    end.reverse()
    # count a
    while start:
        if not s:
            s = start.pop()

        if e == None and len(end) == 0:
            na += 1
            s = None
            continue

        if not e:
            e = end.pop()

        if s < e:
            na += 1
            s = None
        else:
            s = None
            e = None

    s = None
    e = None
    start = b_start
    start.sort()
    start.reverse()
    end = a_end
    end.sort()
    end.reverse()
    # count b
    while start:
        if not s:
            s = start.pop()

        if e == None and len(end) == 0:
            nb += 1
            s = None
            continue

        if not e:
            e = end.pop()

        if s < e:
            nb += 1
            s = None
        else:
            s = None
            e = None

    return na, nb









if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    wfile = open(out_file, 'w')
    case_no = 1
    for na, nb, a_start, a_end, b_start, b_end in read_file(in_file):
        a, b = count_train(na, nb, a_start, a_end, b_start, b_end)
        wfile.write('Case #'+str(case_no)+': '+str(a)+' '+str(b)+'\n')
        case_no += 1

#END