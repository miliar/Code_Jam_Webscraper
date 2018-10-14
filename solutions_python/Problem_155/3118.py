__author__ = 'Sandi'
from collections import defaultdict

def calc(s, m):
    already = 0
    need = 0
    s = str(s)
    d = defaultdict(int)
    cnt = 0
    for i in s:
        d[cnt] = int(i)
        cnt += 1

    for i in range(len(d)):
        #print(need, already)
        tmp = need + already
        if tmp < i:
            need += i - tmp
        already += d[i]

    if need < 0:
        need = 0
    return need

fi = open("input.txt", 'r')
fo = open("output.txt", 'w')
cnt = 0
for f in fi:
    if cnt == 0:
        n = int(f)
    if cnt > 0:
        tmp = f.split()
        res = "Case #"+str(cnt)+": "+ str(calc(tmp[1], int(tmp[0])))
        if cnt < n:
            fo.write(res+"\n")
        else:
            fo.write(res)
    cnt += 1
fi.close()
fo.close()