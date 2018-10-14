import os
f_inp = 'inp_1.txt'
f_out = 'out_1.txt'
f=open(f_inp)
f_o = open(f_out, 'w')
def next_line(f):
    line = f.readline()
    if line:
        line = line.strip()
    return line

def get_matching_set(f, row_num):
    for i in range(0,4):
        line = next_line(f)
        if i == row_num-1:
            s = set(line.split(' '))
    return s

num_tc = int(next_line(f))
bad = 'Bad magician!'
cheat = 'Volunteer cheated!'
resp = 'Case #%s: %s'
for i in xrange(1,num_tc+1):
    row_1 = int(next_line(f))
    s1 = get_matching_set(f, row_1)
    row_2 = int(next_line(f))
    s2 = get_matching_set(f, row_2)
    intersect = s1&s2
    if len(intersect) == 0:
        out = resp % (i, cheat)
    elif len(intersect) == 1:
        out = resp % (i, list(intersect)[0])
    else:
        out = resp % (i, bad)
    f_o.write('%s\n' % out)
    print out
f.close()
f_o.close()
