import sys

def solve(arg):
    args = arg.split()
    itr = enumerate(args)
    c = int(itr.next()[1])
    cmb = {}
    for i in range(c):
        s = itr.next()[1]
        cmb[''.join(sorted(s[0:2]))] = s[2]
    d = int(itr.next()[1])
    opp = {}
    for i in range(d):
        s = itr.next()[1]
        oppe = opp.setdefault(s[0], set())
        oppe.add(s[1])
        oppe = opp.setdefault(s[1], set())
        oppe.add(s[0])
    
    invn = int(itr.next()[1])
    inv = itr.next()[1]
    elist = []
    for i in inv:
        if elist:
            last = elist[-1]
            c = cmb.get(''.join(sorted(last + i)))
            if c:
                elist.pop()
                elist.append(c)
                continue
        oppe = opp.get(i)
        if oppe:
            for e in elist:
                if e in oppe:
                    elist = []
                    break
            else:
                elist.append(i)
        else:
            elist.append(i)
    return elist
        

def main():
    f = open(sys.argv[1])
    n = int(f.next())
    for i in range(n):
        r = solve(f.next())
        print 'Case #%d: [%s]' % (i+1, ', '.join(r))
    

if __name__ == '__main__':
    main()
    