def read(num):
    if num[0] == '1':
        return 1.0
    nums = map(int, list(num[2:]))
    return nums[0] * 1e-1 + nums[1] * 1e-2 + nums[2] * 1e-3 + nums[3] * 1e-4

def main(index):
    print 'Case #%d:' % index,
    N, K = map(int, raw_input().split())
    U = float(raw_input())
    Ps = sorted(map(read, raw_input().split()))
    Cs = [Ps[0]]
    for p in Ps[1:]:
        Cs.append(Cs[-1] + p)
#    print Cs
#    print Ps 
    if U >= Ps[N-1] * N - Cs[N-1]:
        p = (Cs[N-1] + U) / N
        M = p ** N
    else:
        for i in xrange(N-2, 0, -1):
            if U >= Ps[i] * (i+1) - Cs[i]:
                p = (Cs[i] + U) / (i+1)
                M = p ** (i+1)
                for p in Ps[i+1:]:
                    M *= p
                break
        else:
            M = 1
            for p in Ps:
                M *= p
    print M



T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
