__author__ = 'Christian'

#fname = 'test_a.txt'
#fname = 'A-small-attempt0.in'
fname = 'A-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')


def compute_flip(s, K):
    n_flips = 0

    while len(s) >= K:
        try:
            i = s.index('-')
        except ValueError:
            return n_flips
        if i+K > len(s):
            return 'IMPOSSIBLE'
        new_s = ''
        for j in range(K):
            new_s += s[i+j] == '-' and '+' or '-'
        s = new_s+s[i+K:]
        n_flips += 1

    return 'IMPOSSIBLE'


T = int(data[0])
for i in range(T):
    s, k = data[i+1].split(' ')
    K = int(k)
    print >> res_file, "Case #%s: %s" % (i+1, compute_flip(s, K))
    
res_file.close()