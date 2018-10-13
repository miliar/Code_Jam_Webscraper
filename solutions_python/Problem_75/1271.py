import sys

def solve(input, combine, oppose):
    
    pairs = {}
    for p in combine:
        pairs[''.join(sorted(p[:2]))] = p[2:]

    opposed = {}
    for o in oppose:
        o1, o2 = o[0], o[1]
        opposed[o1] = o2
        opposed[o2] = o1

    def mkpair(c1, c2):
        return ''.join(sorted([c1, c2]))

    last = ''
    output = []
    #olist = []
    for ele in input:
        pr = pairs.get(mkpair(last,ele), 0)
        last = ele
        if (pr != 0):
            if len(output)!=0:
                output.pop()
            output.append(pr)
            last = ""
            continue

        op = opposed.get(ele, 0)
        if (op!=0) and (output.count(op)>0):
            output = []
            last = ""
            continue

        output.append(ele)

    return output

if __name__ == '__main__':
    f = open(sys.argv[1])
    T = int(f.readline().strip())
    count = 1
    for line in f:
        combine = []
        oppose = []
        input = ""

        x = line.strip().split()
        c = int(x.pop(0))
        for i in range(c):
             combine.append(x.pop(0))
        d = int(x.pop(0))
        for i in range(d):
             oppose.append(x.pop(0))

        input = x[-1]

        out = solve(input, combine, oppose)
        print "Case #%s: %s"%(count, out)
        count += 1
        if count>T:
            break

