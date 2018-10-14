in_ = open("problem_b_2.in").read().split()
out = open("problem_b_2.out", "w")

cases = int(in_[0])
index = 1
for i in xrange(1, cases + 1):
    num = [int(p) for p in list(in_[i])]
    for x in xrange(len(num) - 1, 0, -1):
        if num[x - 1] > num[x]:
            num[x - 1] = num[x - 1] - 1
            num[x:len(num)] = [9 for e in xrange(len(num) - x)]
    out.write("Case #{}: {}\n".format(i, int(''.join([str(q) for q in num]))))
