def solve():
    T = int(raw_input())
    for test in range(T):
        n = int(raw_input())
        myline = []
        for i in range(4):
            line = map(int,raw_input().split(' '))
            if i == n-1:
                myline = line

        myline2 = []
        n = int(raw_input())
        for i in range(4):
            line = map(int,raw_input().split(' '))
            if i == n-1:
                myline2 = line

        one = set(myline)
        two = set(myline2)
        sz = len(one.intersection(two))
        if sz == 1:
            print "Case #%d: %d" % (test+1, one.intersection(two).pop())
        elif sz > 1:
            print "Case #%d: Bad magician!" % (test+1)
        else:
            print "Case #%d: Volunteer cheated!" % (test+1)

if __name__ == '__main__':
    solve()
