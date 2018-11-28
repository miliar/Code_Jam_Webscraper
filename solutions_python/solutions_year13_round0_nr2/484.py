import sys

def min_height(rect):
    m = 101
    for r in rect:
        m = min(m, min(r))
    return m

def del_min_line(rect, m):
    for i, r in enumerate(rect):
        if min(r) == max(r) == m:
            del rect[i]
            return True
    else:
        return False


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        N, M = [ int(e) for e in sys.stdin.readline().strip().split()]
        rect = [[ int(e) for e in  sys.stdin.readline().strip().split()] for i in range(N)]
        #        print rect
        deleted = True
        while deleted:
            m = min_height(rect)
            deleted = del_min_line(rect, m)
            #print rect
            rect = zip(*rect)
            deleted = (deleted or del_min_line(rect, m))
            #print rect
        if rect:
            print "Case #%d: NO" % (t+1)
        else:
            print "Case #%d: YES" % (t+1)
