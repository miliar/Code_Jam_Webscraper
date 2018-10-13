def main():
    f = open("a.in",  "r")
    ntests = int(f.readline())

    for nt in xrange(1, ntests + 1):
        a = []
        m = []
        for k in xrange(2):
            a.append(int(f.readline()) - 1)
            m.append([f.readline().split() for i in xrange(4)])

        possible_cards = set(m[0][a[0]]) & set(m[1][a[1]])
        if not possible_cards:
            print "Case #%d: Volunteer cheated!" % nt
        elif len(possible_cards) > 1:
            print "Case #%d: Bad magician!" % nt
        else:
            print "Case #%d: %s" % (nt, possible_cards.pop())


if __name__ == "__main__":
    main()
