__author__ = 'lexplua'
fin = open("input.txt", 'r')
fout = open("out.txt", 'w')


def play_war(g, b):
    _g = g[:]
    _b = b[:]
    cnt = 0
    for i in _g:
        x = [j for j in _b if j > i]
        if x != []:
            _b.remove(x[0])
        else:
            cnt += 1
    return cnt


def play_lie(g, b):
    _g = g[:]
    _b = b[:]
    cnt = 0
    for e in _g:
        x = [k for k in _b if k < e]
        if x:
            _b.remove(x[0])
            cnt+=1

    return cnt


n_cases = int(fin.readline().strip())
for n in range(n_cases):
    fout.write("Case #{}: ".format(n + 1))
    fin.readline()
    g = [float(x) for x in fin.readline().strip().split()]
    b = [float(x) for x in fin.readline().strip().split()]
    g.sort()
    b.sort()
    fout.write("%s " % play_lie(g, b))
    fout.write("%s\n" % play_war(g, b))
fin.close()
fout.close()

