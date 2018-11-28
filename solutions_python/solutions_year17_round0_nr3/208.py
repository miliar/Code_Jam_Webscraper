
fo = open("1.out", "w")
fi = open("1.in", "r")
n = int(fi.readline())
for i in range(0, n):
    s = fi.readline()
    a, b = [int(ss) for ss in s.split(' ')]
    c = b
    cnt = 0
    while c > 0:
        c = c / 2
        cnt = cnt + 1
    mod = b - (1 << (cnt-1)) + 1
    last = a - (1 << (cnt-1))+1
    mod_cell = last % (1 << (cnt-1))
    ans_cell = last / (1 << (cnt-1))
    ans_all = ans_cell if mod <= mod_cell else ans_cell-1
    fo.write('Case #{}: {} {}\n'.format(i + 1, ans_all-ans_all/2, ans_all/2))
