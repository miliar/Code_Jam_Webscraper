def test(n):
    n = [i for i in str(n)]
    nlen = len(n)
    num = []
    early = False
    for i in xrange(nlen - 1):
        if int(n[i]) > int(n[i + 1]):
            num += str(int(n[i]) - 1)
            num += '9' * (nlen - i - 1)

            # work backwards
            for j in xrange(i, 0, -1):
                if num[j] < num[j - 1]:
                    num[j] = '9'
                    num[j-1] = str(int(num[j-1]) - 1)
                else:
                    early = True
                    break
            early = True
            break
        else:
            num += n[i]

    if not early:
        num += n[-1]

    if not num:
        num = n[0]
    return int(''.join(num))


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, test(n))
