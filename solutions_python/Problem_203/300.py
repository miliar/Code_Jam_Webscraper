T = int(input())

def fill_col(col):
    first, last = None, None
    res = []
    for x in col:
        if x == '?':
            if last is None:
                res.append(x)
            else:
                res.append(last)
        else:
            first = first or x
            last = x
            res.append(x)

    if first is None:
        return None
    else:
        ii = 0
        while res[ii] == '?':
            res[ii] = first
            ii += 1

        return res


def fill(arr):
    trans = []
    for ii in range(len(arr[0])):
        first = '?'
        col = [x[ii] for x in arr]
        trans.append(fill_col(col))

    for ii in range(len(trans)):
        if trans[ii] is None:
            if ii == 0:
                kk = ii
                while trans[kk] is None:
                    kk += 1

                while kk > ii:
                    trans[kk - 1] = trans[kk]
                    kk -= 1
            else:
                trans[ii] = trans[ii - 1]

    orig = []
    for ii in range(len(trans[0])):
        row = [x[ii] for x in trans]
        orig.append(row)

    return orig


ii = 0
while ii < T:
    ii += 1
    R, C = [int(x) for x in input().split()]
    sq = []
    for j in range(R):
        sq.append([x for x in input()])


    sq = fill(sq)

    # print(sq)

    print("Case #{}:".format(ii))
    for j in range(R):
        print(''.join(sq[j]))

