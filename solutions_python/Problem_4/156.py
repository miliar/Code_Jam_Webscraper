n = input()
cases = []
for i in range(n):
    t = input()
    v1 = raw_input()
    v1 = v1.split()
    v2 = raw_input()
    v2 = v2.split()
    for i in range(len(v1)):
        v1[i],v2[i] = int(v1[i]), int(v2[i])
    v1.sort()
    v2.sort()
    v2.reverse()
    produto = []
    for i in range(len(v1)):
        produto.append(v1[i]*v2[i])
    produto = sum(produto)
    cases.append(produto)

for i in range(n):
    print 'Case #%d: %d' % (i+1, cases[i])
