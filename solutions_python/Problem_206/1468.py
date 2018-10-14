import sys
def main():
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for num in xrange(1, t + 1):
        # read a list of integers, 2 in this case
        D, N = map(int, raw_input().split())
        horses = []
        for i in xrange(1, N + 1):
            k, s = map(int, raw_input().split())
            horses.append((k, s))
        res = helper(D, horses)
        print "Case #{}: {}".format(num, float(D / res))


def helper(D, horses):
    if(len(horses) == 1):
        return (D - horses[0][0]) / float(horses[0][1])
    horses.sort(key = lambda x : x[0])
    id = len(horses) - 1
    t = (D - horses[id][0]) / float(horses[id][1])
    for i in range(len(horses) - 2, -1, -1):
        if(horses[i][1] <= horses[id][1]):
            t2 = sys.maxint
        else:
            t2 = (horses[id][0] - horses[i][0])/float(horses[i][1] - horses[id][1])
        if(t2 > t):
            id = i
            t = (D - horses[id][0]) / float(horses[id][1])
    return t



if __name__ == '__main__':
    main()
