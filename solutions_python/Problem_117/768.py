def main():
    T = int(raw_input())
    for ti in xrange(T):
        NM = [int(x) for x in raw_input().split()]
        N = NM[0]
        M = NM[1]
        lawn = []
        for ni in xrange(N):
            hs = [int(x) for x in raw_input().split()]
            lawn.append(hs)
        new_lawn = [[100 for mi in xrange(M)] for ni in xrange(N)]
        for ni in xrange(N):
            max_h = 0
            for mi in xrange(M):
                if lawn[ni][mi] > max_h:
                    max_h = lawn[ni][mi]
            h = max_h

            for mi in xrange(M):
                if new_lawn[ni][mi] > h:
                    new_lawn[ni][mi] = h
            
        for mi in xrange(M):
            max_h = 0
            for ni in xrange(N):
                if lawn[ni][mi] > max_h:
                    max_h = lawn[ni][mi]
            h = max_h
            for ni in xrange(N):
                if new_lawn[ni][mi] > h:
                    new_lawn[ni][mi] = h
        # print "\n".join([str(x) for x in lawn])
        # print ""
        # print "\n".join([str(x) for x in new_lawn])
        if new_lawn == lawn:
            print "Case #{0}: YES".format(ti+1)
        else:
            print "Case #{0}: NO".format(ti+1)


    pass

if __name__ == "__main__":
    main()
