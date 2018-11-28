import sys

def calc_aver ( T ):
    r = []
    for x in T:
        if len(x[1]) != 0:
            r.append(float(sum(x[1])) / len(x[1]))
        else:
            r.append(0.0)
    NT = []
    for x in T:
        r_list = [r[y] for y in x[0]]
        NT.append((x[0], r_list))
    return r, NT

def calc_owp ( T, IST ):
    r = []
    for j, x in enumerate(T):
        owp_sum = 0.0
        for i, y in enumerate(x[0]):
            if len(IST[y][0]) > 1:
                A = 0 if IST[j][1][i] == 1 else 1
                owp_sum += x[1][i] + ((x[1][i] - A) / (len(IST[y][0]) - 1))
        if len(x[1]) != 0:
            r.append(owp_sum / len(x[1]))
        else:
            r.append(0.0)
    NT = []
    for x in T:
        r_list = [r[y] for y in x[0]]
        NT.append((x[0], r_list))
    return r, NT

in_f = open(sys.argv[1], 'r')
out_f = open(sys.argv[2], 'w')

N = int(in_f.readline())

for i in xrange(N):
    z = int(in_f.readline())
    T = []
    for j in xrange(z):
        s = in_f.readline()
        r_list = []
        command_list = []
        for ii in xrange(len(s)-1):
            if s[ii] != '.':
                r_list.append(float(s[ii]))
                command_list.append(ii)
        T.append((command_list, r_list))
    r1, T2 = calc_aver(T)
    r2, T3 = calc_owp(T2, T)
    r3, T4 = calc_aver(T3)
    out_f.writelines('Case #%d:\n' % (i + 1))
    for x in xrange(z):
        rpi =  r1[x] * 0.25 + r2[x] * 0.5 + r3[x] * 0.25
        out_f.writelines(str(rpi) + '\n')

