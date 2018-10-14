def getArrangement():
    return [ map(int, raw_input().split()) for line in xrange(4) ]
testCases = input()
for i in xrange(testCases):
    answer1, arangement1, answer2, arangement2 = input(), getArrangement(), input(), getArrangement()
    possibilities = set(arangement1[answer1-1]).intersection(set(arangement2[answer2-1]))
    print 'Case #{0}:'.format(i+1),
    if len(possibilities) == 0:
        print 'Volunteer cheated!'
    elif len(possibilities) == 1:
        for poss in possibilities: # only one
            print poss
    else:
        print 'Bad magician!'
