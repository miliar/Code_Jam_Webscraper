import sys;

def solve(inf,outf):
    num = int(inf.readline())
    table = []
    for temp in range(num):
        table.append(inf.readline())
    wp = []
    owp = []
    oowp = []

    for i in range(num):
        total = 0
        win = 0
        for j in range(num):
            if table[i][j] == '1':
                win += 1
                total += 1
            elif table[i][j] == '0':
                total += 1
        if total == 0:
            wp.append(0)
        else:
            wp.append(float(win)/total)

    for i in range(num):
        allw = 0.0
        cnt = 0
        for j in range(num):
            win = 0
            total = 0
            if i == j:
                continue
            if table[i][j] == '.':
                continue
            cnt += 1
            for k in range(num):
                if i == k:
                    continue
                if table[j][k] == '1':
                    win += 1
                    total += 1
                elif table[j][k] == '0':
                    total += 1
            if total != 0:
                allw += float(win)/total
        owp.append(allw /cnt)
    for i in range(num):
        total = 0.0;
        cnt = 0
        for j in range(num):
            if table[i][j] == '.':
                continue
            cnt += 1
            total += owp[j]
        if cnt == 0:
            oowp.append(0)
        else:
            oowp.append(total / cnt)
    print wp
    print owp
    print oowp
    for i in range(num):
        rt = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]
        outf.write(str(rt) + '\n')


if __name__ == '__main__':
    infile = open(sys.argv[1],'r')
    outfile = open(sys.argv[2],'w')
    line = infile.readline()
    cases = int(line)
    for num in range(cases):
        outfile.write('Case #%d:\n' %(num+1))
        solve(infile,outfile)


    infile.close()
    outfile.close()
