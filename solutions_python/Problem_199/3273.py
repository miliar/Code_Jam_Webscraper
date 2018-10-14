flippers = []

min_res = 10000

def build_flipper_array(n, k):
    flippers = []
    for i in range(0, n - k + 1):
        flippers.append(2 ** (k + i) - 2 ** i )
    return flippers


def scan(left, right, cvalue, dest, no):
    global min_res
    #print left, right, cvalue, dest
    if left > right:
        return None
    for i in range(left, right):
        if cvalue ^ flippers[i] == dest:
            #print "res", no
            if no < min_res:
                min_res = no
        else:
            scan(left + 1, right, cvalue ^ flippers[i], dest, no + 1)
            #if r != None:
            #    return r 
    return None


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        min_res = 10000

        blk = raw_input().split(' ')
        
        if not '-' in blk[0]:
            print "Case #{}: {}".format(i, 0)
            continue

        s = ''

        for c in blk[0]:
            if c == '-':
                s += '0'
            else:
                s += '1'

        n = len(s)
        p = int(s, 2)
        k = int(blk[1])
        #print n, k, p
        flippers = build_flipper_array(n, k)
        #print flippers
        scan(0, len(flippers), p, 2 ** n - 1, 1)
        if min_res == 10000:
            print "Case #{}: {}".format(i, "IMPOSSIBLE")
        else:
            print "Case #{}: {}".format(i, min_res)
    #    k = int(raw_input())
    #    print s, k
        # check out .format's specification for more formatting options