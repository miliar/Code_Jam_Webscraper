def solve():
    s = map(int, list(raw_input()))
    if len(s) == 1:
        return int(s[0])

    already_non_decreasing = True
    for i in xrange(len(s) - 1):
        if s[i] > s[i + 1]:
            already_non_decreasing = False
            break
    if already_non_decreasing:
        return int("".join(str(x) for x in s))

    # TODO: 11111...0000
    special = False
    for fixed_index in xrange(len(s) - 1):
        only_ones = True
        for i in xrange(fixed_index + 1):
            if s[i] != 1:
                only_ones = False
                break
        only_zeroes = True
        for i in xrange(fixed_index + 1, len(s)):
            if s[i] != 0:
                only_zeroes = False
                break
        if only_ones and only_zeroes:
            special = True

    if special:
        # print "HERE"
        return int("".join(str(9) for i in xrange(len(s) - 1)))

    # change_found = False
    # idx = 0
    # st_idx = 0
    # for i in xrange(len(s) - 1):
    #     if s[i] > s[i + 1]:
    #         s[i] -= 1
    #         change_found = True
    #         idx = i
    #         break

    lf = 0
    rg = 1
    idx = 1
    while rg < len(s):
        # print lf, rg
        # print s[lf], s[rg]
        if s[lf] > s[rg]:
            s[lf] -= 1
            idx = rg
            break
        if s[lf] != s[rg]:
            if rg - lf > 1:
                lf = rg
                rg = lf + 1
            else:
                lf += 1
                rg += 1
        else:
            rg += 1
        idx = rg


    for i in xrange(lf + 1, len(s)):
        s[i] = 9
    # print s
    return int("".join(str(x) for x in s))

def is_non_dec(val):
    ans_str = str(val)
    already_non_decreasing = True
    for i in xrange(len(ans_str) - 1):
        if ans_str[i] > ans_str[i + 1]:
            already_non_decreasing = False
            break
    if already_non_decreasing:
        return True
    else:
        print val
        return False

def brute():
    x = int(raw_input())
    for i in xrange(x, -1, -1):
        if is_non_dec(i):
            return i

def main():
    t = int(raw_input())
    for qq in xrange(t):
        ans = solve()
        # ans = brute()
        assert(is_non_dec(ans))
        print "Case #{0}: {1}".format(qq + 1, ans)

if __name__ == '__main__':
    main()
