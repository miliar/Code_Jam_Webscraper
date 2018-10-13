import math

def all_nonempty(a):
    for x in a:
        if x == []:
            return(False)
    return(True)

def f1(r, p):  # recipe, package
    # determine max and min numbers for the packages constructable per each
    mx = []
    mn = []

    for pi in range(len(r)):
        mxi = []
        mni = []
        for j in range(len(p[pi])):
            # TODO: rounding!!!
            mxi.append(math.floor(1.0 * p[pi][j] / r[pi] / 0.9))
            mni.append(math.ceil(1.0 * p[pi][j] / r[pi] / 1.1))
        mx.append(sorted(mxi, reverse=True))
        mn.append(sorted(mni, reverse=True))

    # progress from left to right: try to use up maximum candidates
    # in pair with the other max candidates
    # if doesn't work - reduce

    packs = 0
    while all_nonempty(mx):
        # feasibility: if top intervals intersection is non-empty
        mn_top = mn[0][0]
        mx_top = mx[0][0]
        for i in range(1, len(mx)):
            mn_top = max(mn_top, mn[i][0])
            mx_top = min(mx_top, mx[i][0])
        if mn_top <= mx_top:
            packs += 1
            for i in range(len(mx)):
                mx[i] = mx[i][1:]
                mn[i] = mn[i][1:]
        else:
            # find the one(s) with the max minvalue and drop those
            max_min = mn[0][0]
            for i in range(len(mn)):
                if mn[i][0] > max_min:
                    max_min = mn[i][0]
            for i in range(len(mn)):
                if mn[i][0] == max_min:
                    mn[i] = mn[i][1:]
                    mx[i] = mx[i][1:]
        # mn[i] = mn[i][1:]
        # mx[i] = mx[i][1:]
    return(packs)
    # sort by maximum (and minimum)




if __name__ == "__main__":
    test_count = int(raw_input())
    for i in range(test_count):
        n_ing, n_packs = [int(x) for x in raw_input().split()]
        req_ing = [int(x) for x in raw_input().split()]
        amo_pkg = []
        for j in range(n_ing):
            amo_pkg.append([int(x) for x in raw_input().split()])

        print("Case #%d: %s" % (i + 1, f1(req_ing, amo_pkg)))
        
