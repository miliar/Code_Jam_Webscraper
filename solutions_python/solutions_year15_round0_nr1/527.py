__author__ = 'ctynan'

f_in = open('/Users/ctynan/Downloads/A-large.in', 'r')
f_out = open('/Users/ctynan/Downloads/A-large.out', 'w')

T = int(f_in.readline())

for tst in range(T):
    S_max, S = f_in.readline().strip('\n').split(' ')
    Shyness = []

    for i in S:
        Shyness.append(int(i))

    best = 10000
    for j in range(1050):
        good = True
        curStanding = j
        for i, v in enumerate(Shyness):
            needed = i
            if curStanding < i:
                good = False
                break
            else:
                curStanding += v
        if good:
            best = j
            break

    f_out.write(("Case #%i: %i\n" % (tst+1, best)))
