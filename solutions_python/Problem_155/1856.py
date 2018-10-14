import sys

def handle_case(line):
    shy_max, vector = line.split()

    peeps, friends = 0, 0
    for i, p in enumerate(vector):
        if int(p) and peeps < i:
            # add enough people to get these guys to stand
            needed = i - peeps

            # track total people
            peeps += needed

            # track added friends
            friends += needed
        peeps += int(p)
        #print "\t%s:%s:%s:%s" % (peeps, needed, i, p)
    return friends

if __name__ == '__main__':
    cases = int(sys.stdin.readline().strip())

    for i in xrange(1, cases+1):
        line = sys.stdin.readline().strip()
        answer = handle_case(line)
        print "Case #{}: {}".format(i, answer)
