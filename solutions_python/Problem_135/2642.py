with open("magictricksmall.txt", "rb")as f:
    cases = int(f.next().strip())
    answers = []
    for t in xrange(cases):
        first = int(f.next().strip())
        first_rows = []
        for x in xrange(4):
            first_rows.append(f.next().strip().split())
        second = int(f.next().strip())
        second_rows = []
        for x in xrange(4):
            second_rows.append(f.next().strip().split())
        overlap = set(first_rows[first - 1]).intersection(second_rows[second - 1])
        print first_rows[first - 1]
        print second_rows[second - 1]
        print overlap
        if len(overlap) == 1:
            answers.append(list(overlap)[0])
        elif len(overlap) == 0:
            answers.append("Volunteer cheated!")
        else:
            answers.append("Bad magician!")
        print answers

with open("magictrickresult.txt", "wb") as g:
    g.write("\n".join(["Case #%s: %s" % (x + 1, answers[x]) for x in xrange(cases)]))






