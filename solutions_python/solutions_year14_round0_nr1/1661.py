def getcards():
    answer = int(f.readline())
    for row in xrange(0, 4):
        l = f.readline()
        if answer == row + 1:
            cards = [int(x) for x in l.split()]
    return cards

with open("test.txt") as f:
    testcases = int(f.readline())

    for i in xrange(0, testcases):
        first = getcards()
        second = getcards()
        guess = set(first).intersection(set(second))
        if len(guess) == 1:
            outcome = list(guess)[0]
        elif len(guess) == 0:
            outcome = "Volunteer cheated!"
        else:
            outcome = "Bad magician!"
        print "Case #%d:" % (i + 1,), outcome
