EXC_MAX_ALT = 10001


def print_res(resmap):
    for row in resmap:
        print ' '.join([str(x) for x in row])


def find_min(startmap, resmap, row, col, key):
    # Do a depth first search for the min alt and assign it
    # with key if it does not have a key 
    n = startmap[row -1][col] if row  > 0 else EXC_MAX_ALT
    w = startmap[row][col - 1] if col > 0 else EXC_MAX_ALT
    e = startmap[row][col + 1] if col + 1 < len(startmap[0]) else EXC_MAX_ALT
    s = startmap[row + 1][col] if row + 1 < len(startmap) else EXC_MAX_ALT
    
    min_q = min(n, w, e, s)
    r, c = 0, 0
    # print 'At %d, %d: ' % (row, col)
    if startmap[row][col] <= min_q:
        # print 'No min'
        resmap[row][col] = key if resmap[row][col] == -1 else resmap[row][col]
        # print_res(resmap)
        return resmap[row][col]
    elif min_q == n:
        # print 'n is min'
        r, c = row -1, col
    elif min_q == w: 
        # print 'w is min'
        r, c = row, col - 1
    elif min_q == e:
        # print 'e is min'
        r, c = row, col + 1
    elif min_q == s:
        # print 's is min'
        r, c = row + 1, col
    else:
        print 'shouldnt' 
        return # we shouldn't be here
    
    resmap[row][col] = find_min(startmap, resmap, r, c, key)
    # print_res(resmap)
    return resmap[row][col]    


if __name__ == '__main__':
    num_maps = int(raw_input())

    for n in range(num_maps):
        dims = raw_input().split()
        h, w = int(dims[0]), int(dims[1])
        startmap, resmap = [], []
    
        for row in range(h):
            startmap.append([int(x) for x in raw_input().strip().split()])
            resmap.append(w * [-1])

        key = 'a'
        for row in range(h):
            for col in range(w):
                if resmap[row][col] == -1:
                    key = chr(ord(find_min(startmap, resmap, row, col, key)) + 1)
                    

                    
        print 'Case #%d:' % (n + 1)
        print_res(resmap)
            