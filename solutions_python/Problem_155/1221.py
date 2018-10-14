fin = open("input.txt", "r")
fout = open("output.txt", "w")

t = int(fin.readline())
for test in range(t):
    n, a = fin.readline().split()
    n = int(n)
    a = list(map(int, list(a)))
    cur_ans = 0
    cnt = 0
    for i in range(n + 1):
        #print(cnt, end = ' ')
        if i > cnt:
            cur_ans += i - cnt
            cnt = i
        cnt += a[i]
    #print()
    print("Case #%d: %d" % (test + 1, cur_ans), file=fout)
fout.close()
