import random

def solution(i, m, _rows, _cols):

    # Case #14:
    dbg = False

    # for every letter you encounter take up as much space as you can
    rows = list(range(_rows))
    random.shuffle(rows)
    cols = list(range(_cols))
    random.shuffle(cols)

    used = []
    for r in rows:
        for c in cols:

            if dbg: print("row: " + str(r) + " col: " + str(c) + " letter: " + str(m[r][c]))

            maxr, minr = r, r # track height and width
            letter = m[r][c] # get current letter

            if letter in used:
                continue
            else:
                used.append(letter)

            if letter != '?':

                rr = r
                while rr-1 >= 0: # try going up
                    rr = rr-1
                    if m[rr][c] == '?':
                        m[rr][c] = letter
                        minr = rr
                    else:
                        break

                rr = r
                while rr+1 < len(rows): # try going down
                    rr = rr+1
                    if m[rr][c] == '?':
                        m[rr][c] = letter
                        maxr = rr
                    else:
                        break

                if dbg:
                    for rrr in m:
                        print("".join(rrr))

                maxc, minc = c, c
                cc = c
                while cc-1 >= 0: # try to go left
                    cc = cc - 1
                    free = True

                    if dbg: print("    Checking...")
                    for rr in range(minr, maxr+1): # check that all squares are free

                        if dbg: print("    " + str(m[rr][cc]))
                        if m[rr][cc] != '?':
                            if dbg: print("    found non ?")
                            free = False
                            break
                    if free: # all squares are free
                        for rr in range(minr, maxr+1):
                            m[rr][cc] = letter
                            minc = cc
                    else:
                        break

                cc = c
                while cc+1 < len(cols): # try to go right
                    cc = cc + 1
                    free = True
                    for rr in range(minr, maxr+1): # check that all squares are free
                        if m[rr][cc] != '?':
                            free = False
                            break
                    if free: # all squares are free
                        for rr in range(minr, maxr+1):
                            m[rr][cc] = letter
                            maxc = cc
                    else:
                        break

                if dbg:
                    for rrr in m:
                        print("".join(rrr))
    return m

def check(m):
    for i in m:
        if '?' in i:
            return False

    return True

def copy(m):
    mm = []
    for i in m:
        mm.append(i[:])
    return mm

testcases = int(input())
for i in range(testcases):

    print("Case #" + str(i+1) + ":")

    rows, cols = [int(x) for x in input().split(" ")]
    tm = []
    for r in range(rows):
        tm.append( list(input()) )

    m = solution(i, copy(tm), rows, cols)
    while not check(m):
        m = solution(i, copy(tm), rows, cols)

    for r in m:
        print("".join(r))
