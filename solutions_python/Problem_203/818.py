'''
Created on 3/18/17

@author: junkang

'''
import sys
sys.setrecursionlimit(1500)

def loadInput(filename):
    input = []
    row_count = -1
    with open(filename, 'r') as f:
        for idx,l in enumerate(f):
            # print 'line:',l.strip()
            if idx == 0:
                continue
            line = l.strip()
            if len(line) == 0:
                continue
            if row_count == -1:
                assert len(line.split()) == 2, "matrix info line: %s"%(line)
                r, c = int(line.split()[0]), int(line.split()[1])
                # cake = [['' for _ in range(c)] for _ in range(r)]
                cake = []
                row_count = 0
                # print r, c
            elif row_count > -1:
                cake.append(list(line))
                row_count += 1
                # print 'row_count:', row_count
                if row_count == r:
                    row_count = -1
                    r = -1
                    c = -1
                    input.append(cake)
    return input


def hasEmpty(inp):
    R = len(inp)
    C = len(inp[0])

    for r in range(R):
        if '?' in inp[r]:
            return True
    return False

def printCake(cake):
    print '-'*len(cake[0])
    for r in cake:
        print ''.join(r)
    print '-' * len(cake[0])


def isRect(inp,_r,_c):
    # printCake(inp)
    # print '=>', inp[_r][_c]
    ret = _isRect(inp, _r, _c)
    # print "ret:", ret
    return ret

def get_cake_minmax(inp, _r, _c):
    R = len(inp)
    C = len(inp[0])
    r = _r
    c = _c
    cur = inp[r][c]
    while r > 0 and inp[r-1][c] == cur:
        r -= 1
    r_min = min(r, R-1) if r < _r else _r
    r = _r

    while c > 0 and inp[r][c-1] == cur:
        c -= 1
    c_min = min(c, C-1) if c < _c else _c
    c = _c

    while r < R-1 and inp[r+1][c] == cur:
        r += 1
    r_max = max(r, 0) if r > _r else _r
    r = _r

    while c < C-1 and inp[r][c+1] == cur:
        c += 1
    c_max = max(c, 0)  if c > _c else _c
    c = _c

    return r_min, r_max, c_min, c_max

def _isRect(inp, _r, _c):
    R = len(inp)
    C = len(inp[0])
    r = _r
    c = _c
    cur = inp[r][c]
    rc = 0
    cc = 0

    r_min, r_max, c_min, c_max = get_cake_minmax(inp, _r, _c)
    # while r > 0 and inp[r-1][c] == cur:
    #     rc += 1
    #     r -= 1
    # r_min = min(r, R-1) if r < _r else _r
    # r = _r
    #
    # while c > 0 and inp[r][c-1] == cur:
    #     cc += 1
    #     c -= 1
    # c_min = min(c, C-1) if c < _c else _c
    # c = _c
    #
    # while r < R-1 and inp[r+1][c] == cur:
    #     rc += 1
    #     r += 1
    # r_max = max(r, 0) if r > _r else _r
    # r = _r
    #
    # while c < C-1 and inp[r][c+1] == cur:
    #     cc += 1
    #     c += 1
    # c_max = max(c, 0)  if c > _c else _c
    # c = _c

    if r_min > 0 and cur in inp[r_min-1][c_min:c_max+1]:
        return False

    if r_max < R-1 and cur in inp[r_max+1][c_min:c_max+1]:
        return False

    elems = set()
    for i in range(r_min, r_max+1):
        if c_min > 0 and inp[i][c_min-1] == cur:
            return False
        if c_max < C-1 and inp[i][c_max+1] == cur:
            return False
        elems.update(inp[i][c_min:c_max+1])

        if len(elems) > 1:
            return False


    return True

def hasEmptyAround(inp,r,c):

    ret = _hasEmptyAround(inp, r, c)
    print 'hasEmptyAround=======[%d,%d]'%(r,c)
    printCake(inp)
    print 'ret:',ret
    return ret

def _hasEmptyAround(inp, r, c):
    if r-1 > 0 and inp[r-1][c] == '?':
        return True
    if r+1 < len(inp) and inp[r+1][c] == '?':
        return True
    if c - 1 > 0 and inp[r][c-1] == '?':
        return True
    if c + 1 < len(inp[0]) and inp[r][c+1] == '?':
        return True

    # rmin = max(r-1, 0)
    # rmax = min(r+1, len(inp))
    # cmin = max(c-1, 0)
    # cmax = min(c+1, len(inp[0]))
    #
    # for i in range(rmin, rmax+1):
    #     if '?' in inp[i][cmin:cmax+1]:
    #         return True

    return False

def fill_icings(inp, _r, _c, visited=None):
    R = len(inp)
    C = len(inp[0])

    print ''
    print _r, _c
    printCake(inp)

    # exit condition: no empty cell
    if not hasEmpty(inp):
        return inp

    for r in range(R):
        for c in range(C):
            # if r < _r or (r == _r and c < _c):
            #     continue
            if inp[r][c] == '?':
                continue

            key = '%d_%d'%(r,c)
            if key in visited and not hasEmptyAround(inp, r, c):
                continue

            cur = inp[r][c]
            next_c = (c + 1) % C

            visited.append(key)

            # up, down, right, left
            # left
            if c > 0 and inp[r][c-1] == '?':
                inp[r][c-1] = cur
                ret = fill_icings(inp, r, next_c, visited[:]) if isRect(inp, r, c) else None
                if ret is None:
                    inp[r][c - 1] = '?'
                else:
                    return ret

            # right
            if c < C-1 and inp[r][c+1] == '?':
                inp[r][c+1] = cur
                ret = fill_icings(inp, r, next_c, visited[:]) if isRect(inp, r, c) else None
                if ret is None:
                    inp[r][c + 1] = '?'
                else:
                    return ret

            # up
            if r > 0 and inp[r-1][c] == '?':
                inp[r-1][c] = cur
                ret = fill_icings(inp, r, next_c, visited[:]) if isRect(inp, r, c) else None
                if ret is None:
                    inp[r - 1][c] = '?'
                else:
                    return ret

            if r < R-1 and inp[r+1][c] == '?':
                inp[r+1][c] = cur
                ret = fill_icings(inp, r, next_c, visited[:]) if isRect(inp, r, c) else None
                if ret is None:
                    inp[r + 1][c] = '?'
                else:
                    return ret

            # diagonal: right down
            if r < R-1 and c < C-1 and inp[r+1][c] == '?' and inp[r][c+1] == '?' and inp[r+1][c+1] == '?':
                inp[r+1][c] = cur
                inp[r][c+1] = cur
                inp[r+1][c+1] = cur
                ret = fill_icings(inp, r, next_c, visited[:]) if isRect(inp, r, c) else None
                if ret is None:
                    inp[r + 1][c] = '?'
                    inp[r][c + 1] = '?'
                    inp[r + 1][c + 1] = '?'
                else:
                    return ret

            # diagonal: left down
            if r < R-1 and c > 0 and inp[r][c-1] == '?' and inp[r+1][c-1]=='?' and inp[r+1][c] == '?':
                inp[r][c-1] = cur
                inp[r+1][c-1] = cur
                inp[r+1][c] = cur
                ret = fill_icings(inp, r, next_c, visited[:]) if isRect(inp, r, c) else None
                if ret is None:
                    inp[r][c - 1] = '?'
                    inp[r + 1][c - 1] = '?'
                    inp[r + 1][c] = '?'
                else:
                    return ret

            # diagonal: right up
            if r > 0 and c < C-1 and inp[r-1][c] == '?' and inp[r][c+1] == '?' and inp[r-1][c+1] == '?':
                inp[r-1][c] = cur
                inp[r][c+1] = cur
                inp[r-1][c+1] = cur
                ret = fill_icings(inp, r, next_c, visited[:]) if isRect(inp, r, c) else None
                if ret is None:
                    inp[r - 1][c] = '?'
                    inp[r][c + 1] = '?'
                    inp[r - 1][c + 1] = '?'
                else:
                    return ret

            # diagonal: left up
            if r > 0 and c > 0 and inp[r][c-1] == '?' and inp[r-1][c-1]=='?' and inp[r-1][c] == '?':
                inp[r][c-1] = cur
                inp[r-1][c-1] = cur
                inp[r-1][c] = cur
                ret = fill_icings(inp, r, next_c, visited[:]) if isRect(inp, r, c) else None
                if ret is None:
                    inp[r][c - 1] = '?'
                    inp[r - 1][c - 1] = '?'
                    inp[r - 1][c] = '?'
                else:
                    return ret

            if isRect(inp, r, c):
                r_min, r_max, c_min, c_max = get_cake_minmax(inp, r, c)
                if r_min > 0:
                    hist = inp[r_min-1][c_min:c_max+1]
                    hist_set = set(hist)
                    if len(hist_set) == 1 and '?' in hist_set:
                        inp[r_min-1][c_min:c_max+1] = [cur]*(c_max-c_min+1)

                        ret = fill_icings(inp, r, next_c, visited[:])
                        if ret is None:
                            inp[r_min - 1][c_min:c_max + 1] = hist
                        else:
                            return ret

                if r_max +1 < R:
                    hist = inp[r_max + 1][c_min:c_max + 1]
                    hist_set = set(hist)
                    if len(hist_set) == 1 and '?' in hist_set:
                        inp[r_max + 1][c_min:c_max + 1] = [cur] * (c_max - c_min + 1)

                        ret = fill_icings(inp, r, next_c, visited[:])
                        if ret is None:
                            inp[r_max + 1][c_min:c_max + 1] = hist
                        else:
                            return ret


    return None


def saveOutput(outputs, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(outputs))
    print '- output:', filename

if __name__ == '__main__':
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/1a/A-large-practice.in', '/Users/junkang/Projects/codejam/qual_A/A-large-practice.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/1A/A-large.in', '/Users/junkang/Projects/codejam/qual_A/A-large.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/1A/A-small-attempt1.in', '/Users/junkang/Projects/codejam/qual_A/A-small-attempt1.out'
    filename_in, filename_out = '/Users/junkang/Projects/codejam/1A/A-small-attempt0.in', '/Users/junkang/Projects/codejam/1A/A-small-attempt0.out'
    # filename_in, filename_out = '/Users/junkang/Projects/codejam/1A/test', '/Users/junkang/Projects/codejam/1A/test.out'

    input = loadInput(filename_in)

    print input
    outputs = []
    for i, inp in enumerate(input):

        printCake(inp)
        ret = fill_icings(inp, 0, 0, [])
        if ret is None:
            print 'Case #%d: FAILED'%(i+1)
            sys.exit()

        msg = []
        for r in ret:
            msg.append(''.join(r))

        output = 'Case #%d: \n%s'%(i+1, '\n'.join(msg))

        print output
        outputs.append(output)

    saveOutput(outputs, filename_out)
