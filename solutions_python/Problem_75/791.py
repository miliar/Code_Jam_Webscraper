#!/usr/bin/python

def combine(s):
    global CD
    if s[-2:] in CD:
        return combine(s[:-2]+CD[s[-2:]])
    return s


if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        ln = f.readline().strip().split()
        C = int(ln[0])
        CL = ln[1:1+C]
        CD = dict(map(lambda x:(x[:2],x[2]), CL))
        CD.update(dict(map(lambda x:(x[1]+x[0],x[2]), CL)))
        D = int(ln[1+C])
        DL = ln[2+C:2+C+D]
        Nstr = ln[3+C+D]
        curr = Nstr[0]
        for j in range(1,len(Nstr)):
            curr += Nstr[j]

            if len(curr) == 1:
                continue
            curr = combine(curr)
            if len(curr) > 1:
                for delpair in DL:
                    a, b = list(delpair)
                    if a in curr and b in curr:
                        curr = ''
                        break

        print 'Case #%d: [%s]'%(i+1,', '.join(list(curr)))



    

