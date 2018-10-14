def update_memo(vine_num, swing_len, memo):
    memo[vine_num] = swing_len

def check_memo(vine_num, swing_len, memo):
    if vine_num not in memo:
        return None
    if memo[vine_num] >= swing_len:
        return False
    return None

def build_solution(dvines, lvines, dtot):
    #build backwards
    swing_min = [None] * len(dvines)
    swing_min[-1] = dtot - dvines[-1]

    if swing_min[-1] > lvines[-1]:
        swing_min[-1] = None

    for i in range(len(dvines)-1, -1, -1):
        gap = dtot - dvines[i]
        if gap <= lvines[i]:
            swing_min[i] = gap
        for j in range(i+1, len(dvines)):
            gap = dvines[j] - dvines[i]
            if gap > lvines[i]:
                break
            if swing_min[j] is None:
                continue
            if swing_min[j] > gap:
                continue
            sm = max(gap, swing_min[j])
            if swing_min[i] is None:
                swing_min[i] = sm
            else:
                swing_min[i] = min(swing_min[i], sm)
    assert i == 0, i
    return swing_min

def can_solve(vine_num, swing_len, dvines, lvines, dtot, memo=None):
    sm = build_solution(dvines, lvines, dtot)
    print sm
    return sm[0] is not None and sm[0] <= min(dvines[0], lvines[0])

    memo = memo or {}
    mc = check_memo(vine_num, swing_len, memo)
    if mc is not None:
        return mc

    #base case
    if dvines[vine_num] + swing_len >= dtot:
        return True

    #which vines can we reach?
    for i in range(vine_num + 1, len(dvines))[::-1]:
        gap = dvines[i] - dvines[vine_num]
        assert gap > 0, gap
        if gap > swing_len:
            #break
            continue
        sprime = min(swing_len, lvines[i], gap)
        if can_solve(i, sprime, dvines, lvines, dtot, memo):
            return True

    update_memo(vine_num, swing_len, memo)
    return False

def solve(ds, ls, dtot):
    return can_solve(0, min(ds[0], ls[0]), ds, ls, dtot)

def test():
    dvs = [3, 4, 6]
    lvs = [4, 10, 10]
    dtot = 9
    print solve(dvs, lvs, dtot)


    ds = [3, 4, 7]
    ls = [4, 10, 10]
    dtot = 9
    print solve(ds, ls, dtot)

    ds = [6, 10]
    ls = [6, 3]
    dtot = 13
    print solve(ds, ls, dtot)

    ds = [6, 10]
    ls = [6, 3]
    dtot = 14
    print solve(ds, ls, dtot)

def main():
    from sys import argv

    data = open(argv[1]+'.in').readlines()
    with open(argv[1]+'.out', 'w') as outfile:
        ntest = int(data[0].strip())
        data = data[1:]
        for i in range(ntest):
            nvine = int(data[0].strip())
            ds, ls = [], []
            for j in range(nvine):
                d,l = map(int, data[j+1].strip().split())
                ds.append(d)
                ls.append(l)
            dtot = int(data[j+2].strip())
            if solve(ds, ls, dtot):
                outfile.write("Case #%i: YES\n" % (i+1))
                print "Case #%i: YES" % (i+1)
            else:
                outfile.write("Case #%i: NO\n" % (i+1))
                print "Case #%i: NO" % (i+1)
            data = data[j+3:]

if __name__ == "__main__":
    #test()
    main()
