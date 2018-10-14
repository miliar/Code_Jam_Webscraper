def solve(N, R, O, Y, G, B, V):
    if R > Y + B or Y > R + B or B > R + Y:
        return "IMPOSSIBLE"
    d = {'R': R,
         'Y': Y,
         'B': B}
    mx = 0
    mxk = ''
    for k in d.keys():
        if d[k] > mx:
            mx = d[k]
            mxk = k
    ans = mxk
    d[mxk] -= 1  # TODO WTF
    for i in range(N-1):
        mx = 0
        mxk = ''
        for k in d.keys():
            if (k != ans[-1]) and ((d[k] > mx) or d[k] == mx and k == ans[0]):
                mx = d[k]
                mxk = k
        if mxk == '':
            print ans
        d[mxk] -= 1
        ans += mxk
    # if ans[0] == ans[-1]:
    #     return "!"
    return ans


def main():
    # f_in = open('B-small-test.in')
    f_in = open('B-small-attempt4.in')
    # f_in = open('B-large.in')
    f_out = open('B-small.out', 'w')
    # f_out = open('B-large.out', 'w')
    T = int(f_in.readline())
    for t in range(T):
        N, R, O, Y, G, B, V = [int(i) for i in f_in.readline().split()]
        s = solve(N, R, O, Y, G, B, V)
        f_out.write("Case #{}: {}\n".format(t+1, s))
        print "Case #{}: {}\n".format(t+1, s),
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
