from collections import defaultdict

quaternion = {'1':{'1':'1','i':'i','j':'j','k':'k'}, 'i':{'1':'i','i':'-1','j':'k','k':'-j'}, 'j':{'1':'j','i':'-k','j':'-1','k':'i'}, 'k':{'1':'k','i':'j','j':'-i','k':'-1'}}

def multstring(first,second):
    negative = (first[0]=='-' and second[0]!='-') or (first[0]!='-' and second[0]=='-')
    first = quaternion[first[-1]][second[-1]]
    if negative and first[0]=='-':
        return first[-1]
    elif negative:
        return '-'+first
    else:
        return first

def dijkstra():
    fields = raw_input().strip().split(' ')
    base = raw_input().strip()
    full = base * int(fields[1])
    i_ends = []
    j_ends = []
    k_starts = []
    results = defaultdict(dict)
    basis = '1'
    prev = '1'
    i_found = False
    prev_istart = 0
    for i in xrange(len(full)):
        curchar = full[i]
        basis = multstring(basis, curchar)
        if i!=prev_istart:
            results[prev_istart][i] = basis
        if i!=0:
            results[i-1][i] = multstring(prev, curchar)
        if not i_found and basis=='i':
            i_found = True
            i_ends.append(i)
            basis = '1'
            prev_istart = i+1
        elif i_found:
            if basis=='1':
                i_ends.append(i)
                basis = '1'
                prev_istart = i+1
            elif basis=='j':
                j_ends.append(i)
    basis = '1'
    k_found = False
    for i in xrange(len(full)-1,-1,-1):
        curchar = full[i]
        basis = multstring(curchar, basis)
        if (not k_found and basis=='k') or (k_found and basis=='1'):
            k_found = True
            if i-1 in j_ends:
                return 'YES'
            basis = '1'
    return 'NO'

ncases = int(raw_input().strip())
for i in xrange(ncases):
    print "Case #{0}: {1}".format(i+1, dijkstra())
