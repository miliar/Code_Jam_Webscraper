import sys


def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        s, k = map(int, raw_input().split())
        ls = [_ for _ in range(s)]
        rs = [_ for _ in range(s - 1, -1, -1)]
        occupied = [0] * s
        y, z = helper(s, k, occupied, ls, rs)
        print "Case #{}: {} {}".format(num, y, z)


def helper(s, k, occupied, ls, rs):
    if(s == k):
        return 0, 0
    while(k != 0):
        min_maxval = 0
        min_maxlist = []
        max_maxval = 0
        max_maxlist = []
        for i in range(s):
            if(not occupied[i]):
                min_maxval = max(min_maxval, min(ls[i], rs[i]))
        for i in range(s):
            if(not occupied[i]) and min_maxval == min(ls[i], rs[i]):
                min_maxlist.append(i)
        if(len(min_maxlist) == 1):
            index = min_maxlist[0]
            set(min_maxlist[0], occupied, ls, rs)
            k -= 1
            continue
        for i in min_maxlist:
            if(not occupied[i]):
                max_maxval = max(max_maxval, max(ls[i], rs[i]))
        for i in min_maxlist:
            if(not occupied[i]) and max_maxval == max(ls[i], rs[i]):
                max_maxlist.append(i)
        index = max_maxlist[0]
        set(index, occupied, ls, rs)
        k -= 1
    return max(ls[index], rs[index]), min(ls[index], rs[index])


def set(index, occupied, ls, rs):
    occupied[index] = 1
    for i in range(index + 1, len(occupied)):
        if(occupied[i] == 1):
            break
        ls[i] = i - index - 1
    for i in range(index - 1, -1, -1):
        if(occupied[i] == 1):
            break
        rs[i] = index - i - 1
if __name__ == '__main__':
    main()
