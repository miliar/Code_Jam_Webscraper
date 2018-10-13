# go to first minus. call this pos
# if len(x) - pos < size: impossible
# else, flip
# repeat


with open('A-large.in') as f:
    f.readline()
    casecount = 1
    for l in f:
        x = list(l.split()[0])
        size = int(l.split()[1])
        cnt = 0
        casestr = 'Case #{}:'.format(casecount)
        while True:
            pos = -1
            for i in range(len(x)):
                if x[i] == '-':
                    pos = i
                    break
            if pos == -1:
                print '{} {}'.format(casestr, cnt)
                break
            if len(x) - pos < size:
                print '{} IMPOSSIBLE'.format(casestr)
                break
            else:
                cnt += 1
                for i in range(size):
                    if x[pos+i] == '-':
                        x[pos+i] = '+'
                    else:
                        x[pos+i] = '-'
        casecount += 1