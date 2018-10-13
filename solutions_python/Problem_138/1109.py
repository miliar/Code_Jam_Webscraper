import os
f_inp = 'inp_4.txt'
f_out = 'out_4.txt'
f=open(f_inp)
f_o = open(f_out, 'w')
def next_line(f):
    line = f.readline()
    if line:
        line = line.strip()
    return line

def get_deceit(n, k):
    index_n=0
    index_k=0
    len_k = len(k) - 1
    count = 0
    while index_n < len(n):
        if n[index_n] > k[index_k]:
            count += 1
            index_k += 1
        index_n += 1
    return count

def get_war(n ,k):
    index_n=0
    index_k=0
    while index_k < len(k):
        while index_k < len(k) and n[index_n] > k[index_k]:
            index_k += 1
        if index_k >= len(k):
            break
        index_n += 1
        index_k += 1
    return len(n) - index_n

num_tc = int(next_line(f))
resp = 'Case #%s: %s %s'
for i in xrange(1,num_tc+1):
    num = int(next_line(f))
    n = [float(_) for _ in next_line(f).split(' ')]
    n = sorted(n)
    k = [float(_) for _ in next_line(f).split(' ')]
    k = sorted(k)
    d = get_deceit(n, k)
    w = get_war(n, k)
    print n,'\n', k
    out = resp % (i, d, w)
    f_o.write('%s\n' % out)
    print out
f.close()
f_o.close()
