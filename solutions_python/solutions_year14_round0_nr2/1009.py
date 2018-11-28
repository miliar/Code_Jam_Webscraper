if __name__ == '__main__':
    infile = 'D:\B-large.in'
    outfile = 'D:\output.txt'
    outlns = []
    lns = [ln.strip() for ln in open(infile).readlines() if ln.strip() != '']

    cases = int(lns[0])
    for i in range(cases):
        cells = lns[i+1].split(' ')
        C = float(cells[0])
        F = float(cells[1])
        X = float(cells[2])
        v_init = 2.0

        time = X/v_init
        reused_factors = 0.0
        v_next = v_init
        while(True):
            reused_factors += C/v_next
            v_next += F
            temp = reused_factors + X/v_next
            if temp < time:
                time = temp
            elif temp == time:
                continue
            else:
                break
        outlns.append('Case #' + str(i+1) + ': ' + '{0:0.7f}'.format(time) + '\n')

    f = open(outfile, 'w')
    f.writelines(outlns)
    f.close()
