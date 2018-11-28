f = open('pancake.in', 'r')
out = open('pancake.out', 'w')
f.readline()
test_case = 1
for l in f:
    k = int(l.split(' ')[1])
    seq = list(l.split(' ')[0])

    def flip(p):
        if p + k > len(seq):
            return False

        for i in range(p, p + k):
            if seq[i] == '-':
                seq[i] = '+'
            else:
                seq[i] = '-'
        return True

    possible = True
    numflips = 0
    for i in range(len(seq)):
        if seq[i] == '-':
            possible = flip(i)
            if not possible:
                break
            numflips += 1
    out.write("Case #{}: ".format(test_case))
    if possible:
        out.write("{}\n".format(numflips))
    else:
        out.write("IMPOSSIBLE\n")
    test_case += 1
