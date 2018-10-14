from sys import stdin

def get_max_index(bsize, first, prev):
    cur_max = 0
    cur_max_ind = None
    for i in range(3):
        if i != prev:
            if bsize[i] > cur_max:
                cur_max = bsize[i]
                cur_max_ind = i
            elif bsize[i] == cur_max and first is not None and first == i:
                cur_max_ind = i
    return cur_max_ind

def other_exist(cols, ind1, ind2):
    for j, el in enumerate(cols):
        if j != ind1 and j != ind2:
            if el != 0:
                return True
    return False

def get_answer():
    parts = [int(el) for el in stdin.readline().strip().split()]
    n = parts[0]
    cols = parts[1:]
    bcols = []
    bsize = []
    cmap = ["B", "R", "Y"]
    special = ["O", "G", "V"]
    for j, i in enumerate([1, 3, 5]):
        if cols[i] != 0:
            if cols[(i + 3) % 6] < cols[i] + 1:
                if cols[(i + 3) % 6] < cols[i] or other_exist(cols, i, (i + 3) % 6):
                    return "IMPOSSIBLE"
                else:
                    return "".join([special[j] + cmap[j]] * cols[i])
            bcols.append(cols[(i + 3) % 6] - cols[i])
            bsize.append(cols[i])
        else:
            bcols.append(cols[(i + 3) % 6])
            bsize.append(0)
    res = []

    first = None
    used = [False, False, False]
    prev = None
    while max(bcols) > 0:
        ind = get_max_index(bcols, first, prev)
        prev = ind
        if ind is None:
            return "IMPOSSIBLE"
        if first is None:
            first = ind
        res.append(cmap[ind])
        bcols[ind] -= 1
        if not used[ind]:
            combined = "".join([special[ind] + cmap[ind]] * bsize[ind])
            if combined != []:
                res.extend([combined])
            used[ind] = True
    if res[0] == res[-1]:
        return "IMPOSSIBLE"
    return "".join(res)

def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print "Case #{0}: {1}".format(i + 1, get_answer())

if __name__ == "__main__":
    main()
