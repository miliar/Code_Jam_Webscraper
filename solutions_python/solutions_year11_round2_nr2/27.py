import sys;

def solve(inf,outf):
    cd = [int(x) for x in inf.readline().split(' ')]
    c = cd[0]
    d = cd[1]
    p = []
    v = []
    cnt = []
    cntv = 0
    for i in range(c):
        pv = [int(x) for x in inf.readline().split(' ')]
        p.append(pv[0])
        v.append(pv[1])
        cnt.append(cntv);
        cntv += pv[1];
    maxtime = 0.0
    for vvalue in v:
        dis = float((vvalue - 1) * d) / 2.0;
        if dis > maxtime:
            maxtime = dis

    for i in range(len(p)):
        for j in range(i+1,len(p)):
            curd = p[j] - p[i]
            curv = cnt[j] - cnt[i] + v[j]
            total = (curv - 1) * d
            if total < curd:
                continue;
            rt = float(total - curd) / 2.0
            if rt > maxtime:
                maxtime = rt
    outf.write(str(maxtime) + '\n')


if __name__ == '__main__':
    infile = open(sys.argv[1],'r')
    outfile = open(sys.argv[2],'w')
    line = infile.readline()
    cases = int(line)
    for num in range(cases):
        outfile.write('Case #%d: ' %(num+1))
        solve(infile,outfile)


    infile.close()
    outfile.close()
