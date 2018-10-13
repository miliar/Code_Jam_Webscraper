with open('A-small-attempt0.in', 'r') as f, open('Magic Trick Result.dat', 'w') as res:
    test_cases_count = int(f.readline())

    for i in xrange(1, test_cases_count + 1):
        card_row_1 = int(f.readline())
        for _ in xrange(card_row_1):
            line = f.readline()
        row_1 = set(line.split())
        for _ in xrange(4 - card_row_1):
            f.readline()

        card_row_2 = int(f.readline())
        for _ in xrange(card_row_2):
            line = f.readline()
        row_2 = set(line.split())
        for _ in xrange(4 - card_row_2):
            f.readline()

        result = row_1 & row_2
        len_result = len(result)
        if (len_result == 1):
            res.write('Case #%d: %s\n' % (i, result.pop()))
        elif (len_result > 1):
            res.write('Case #%d: %s\n' % (i, 'Bad magician!'))
        else:
            res.write('Case #%d: %s\n' % (i, 'Volunteer cheated!'))
