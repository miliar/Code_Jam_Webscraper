__author__ = 'Levan Kasradze'

with open('a.in', 'r') as fin:
    with open('a.out', 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t + 1):
            fout.write('Case #' + str(i) + ': ')
            s = fin.readline().split()
            cnt = 0
            cur = int(s[1][0])
            for i in range(1, len(s[1])):
                if s[1][i] == '0':
                    continue
                if cur < i:
                    cnt += i - cur
                    cur += i - cur
                cur += int(s[1][i])

            fout.write(str(cnt) + '\n')