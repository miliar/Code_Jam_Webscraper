import re

f = open("A-small-attempt0.in")
N = int(f.readline())


fout = open("A-small.out", "w")
for case in range(1, N+1):
    L = int(f.readline())
    tree = ''.join([','.join(f.readline().split()) for i in range(L)])
    new = ''
    for i in range(len(tree)):
        if i and tree[i] == '(':
            new += ',('
        else:
            new += tree[i]
    tree = new
    tree = tree.replace('(,', '(')
    tree = re.sub('[a-z]+', lambda x: '"'+x.group(0)+'"', tree)
    tree = re.sub('(?<!,)\)', ',)', tree)
    t = eval(tree)

    A = int(f.readline())
    animals = []
    for i in range(A):
        line = f.readline().split()
        animals.append([line[0], set(line[2:])])

    fout.write("Case #%d:\n" % case)
    for a in animals:
        cur = t
        p = 1
        while 1:
            p *= cur[0]
            if len(cur) == 1:
                break

            if cur[1] in a[1]:
                cur = cur[2]
            else:
                cur = cur[3]
        fout.write('%f\n' % p)

fout.close()
