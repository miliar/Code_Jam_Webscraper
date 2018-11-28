in_f = open('A-small-attempt0.in.txt', 'r')
out_f = open('A-small-attempt0.out.txt', 'w')

t = int(in_f.readline())
print t

for i in range(t):
    f_m = []
    s_m = []
    f_i = int(in_f.readline())
    for f in range(1,5):
        line = in_f.readline()
        if f == f_i:
            line = line.split(' ')
            for str_n in line:
                f_m.append(int(str_n))
    s_i = int(in_f.readline())
    for f in range(1,5):
        line = in_f.readline()
        if f == s_i:
            line = line.split(' ')
            for str_n in line:
                s_m.append(int(str_n))
    result = 0
    result_count = 0
    for f in f_m:
        for s in s_m:
            if f == s:
                result = f
                result_count += 1
    out_f.write('Case #%d: ' % (i+1))
    if result_count == 0:
        out_f.write('Volunteer cheated!')
    elif result_count > 1:
        out_f.write('Bad magician!')
    else:
        out_f.write('%d' % result)
    out_f.write('\n')

in_f.close();
out_f.close();
