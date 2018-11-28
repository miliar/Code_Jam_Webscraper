


def main():
    ncases = int(raw_input())
    for i in xrange(ncases):
        answer_1 = int(raw_input())
        for j in xrange(4):
            if j+1 == answer_1:
                possibilities = set(raw_input().split(" "))
            else:
                raw_input()
        answer_2 = int(raw_input())
        for j in xrange(4):
            if j+1 == answer_2:
                card = raw_input().split(" ")
            else:
                raw_input()
        # If no cards are in possibilities volunteer cheated
        # If two cards are in possibilities magician failed
        # If exactly one card in possibilities deal
        matches = []
        for c in card:
            if c in possibilities:
                matches.append(c)
        if not matches:
            print "Case #%d: Volunteer cheated!"%(i+1)
        elif len(matches) > 1:
            print "Case #%d: Bad magician!"%(i+1)
        else:
            print "Case #%d: %d" %(i+1,int(matches[0]))

if __name__ == '__main__':
    main()
