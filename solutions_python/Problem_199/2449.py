INPUT_FILE_NAME = 'A-large.in'
OUTPUT_FILE_NAME = 'out'

fin = open(INPUT_FILE_NAME)
fout = open(OUTPUT_FILE_NAME, 'w')

def f(s, k):
    ans = 0
    s = list(s)
    for i in range(0, len(s) - k + 1):
        if (s[i] == '-'):
            ans += 1
            for j in range(i, i + k):
                if s[j] == '-': s[j] = '+'
                else: s[j] = '-'
    for c in s:
        if c == '-':
            return 'IMPOSSIBLE'
    return ans

for case in xrange(1, 1 + int(fin.readline())):
    l = fin.readline()
    t = l.split()
    s = t[0]
    k = int(t[1])
    fout.write("Case #{0}: {1}\n".format(case, f(s, k)))

fout.close()
fin.close()
