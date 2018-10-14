# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
# 5
# 4 2
# 5 2
# 6 2
# 1000 1000
# 1000 1

def _calc_counts(stall_occupancy):
    # count left to right for ls
    n = len(stall_occupancy)
    s = [None] * n
    count = 0
    for i in range(0, len(stall_occupancy)):
        if not stall_occupancy[i]:
            s[i] = count
            count += 1
        else:
            count = 0
    return s

def _calc_ls(stall_occupancy):
    return _calc_counts(stall_occupancy)
def _calc_rs(stall_occupancy):
    return list(reversed(_calc_counts(list(reversed(stall_occupancy)))))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    (n, k) = input().split()
    n = int(n)
    k = int(k)
    #print("Case #{}: INPUT n:{} k:{}".format(i, n, k))

    occupancy = [False] * n
    for person in range(0, k):

        ls = _calc_ls(occupancy)
        rs = _calc_rs(occupancy)


        #print('ls:%s' % ls)
        #print('rs:%s' % rs)
        min_lsrs = list(map(lambda x, y: x and y and min([x, y]), ls, rs))
        #print('min_lsrs:%s' % min_lsrs)

        m = max(x for x in min_lsrs if x is not None)
        loc_1 = [i for i, j in enumerate(min_lsrs) if j == m]
        #print("loc_1:%s" % loc_1)
        if len(loc_1) == 1:
            #print("Method1 success")
            ix = loc_1[0]
        else:
            #print("Method2 ")
            ls_ = [ls[index] for index in loc_1]
            rs_ = [rs[index] for index in loc_1]
            #print("ls_:%s" % ls_)
            #print("rs_:%s" % rs_)
            max_lsrs = list(map(lambda x, y: max([x, y]), ls_, rs_))
            #print("max_lsrs:%s" % max_lsrs)
            m = max(max_lsrs)
            loc_2 = [i for i, j in enumerate(max_lsrs) if j == m]
            #print("loc_2:%s" % loc_2)
            ix = loc_1[loc_2[0]]

        #print("Person:%d" % person)
        #print("Occupancy:before:%s" % occupancy)
        occupancy[ix] = True
        #print("Cccupancy:after: %s" % occupancy)
        y = max([ls[ix], rs[ix]])
        z = min([ls[ix], rs[ix]])

    print("Case #{}: {} {}".format(i, y, z))