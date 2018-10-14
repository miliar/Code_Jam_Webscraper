fin = open('B-small-attempt0.in', 'r')
fout = open('output.txt', 'w')
t = int(fin.readline())
for case in range(t):
    ans = 0
    line = fin.readline().strip('\n').split()
    n = int(line[0])
    s = int(line[1])
    p = int(line[2])
    a = sorted([int(num) for num in line[3:]], reverse=True)
    for k in a:
        q = k / 3
        r = k % 3
        if q >= p:
            ans += 1
        elif q == p - 1:
            if r == 1 or r == 2:
                ans += 1
            else:
                if s > 0 and q > 0:
                    ans += 1
                    s -= 1
        elif q == p - 2:
            if r == 2 and s > 0 and q > 0:
                ans += 1
                s -= 1

    fout.write('Case #{:d}: {:d}\n'.format(case+1, ans))
fin.close()
fout.close()
