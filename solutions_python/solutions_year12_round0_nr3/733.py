#inf = open('/home/nullard/Downloads/C-small-attempt0.in')
inf = open('/home/nullard/Downloads/C-large.in')
#inf = open('../data/problemc.in')
outf = open('../data/problemc.ot', 'w')
def op(s):
    print s
    outf.write(s + '\n')

num_cases = int(inf.readline().strip())

for i in range(1, num_cases + 1):
    a, b = map(int, inf.readline().split())
    pairs = 0
    btest = str(b)
    for j in range(a, b + 1):
        s = str(j)
        for k in range(1, len(s)):
            s2 = s[k:] + s[:k]
            if s2 == s: break
            elif s2 > s and s2 <= btest: 
                pairs += 1
            
    op('Case #' + str(i) + ': ' + str(pairs))