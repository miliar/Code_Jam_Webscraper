def solve(answers, arrangements):

    # Some constants
    BAD_MAGICIAN = u"Bad Magician!"
    VOLUNTEER_CHEATED = u"Volunteer cheated!"
    
    # Compute set of cards in row of first answer.
    first_guess = set(arrangements[0][answers[0]-1])
    second_guess = set(arrangements[1][answers[1]-1])

    intersection = first_guess & second_guess
    number_of_possible_cards = len(intersection)

    if number_of_possible_cards == 1:
        return unicode(list(intersection)[0])
    elif number_of_possible_cards == 0:
        return VOLUNTEER_CHEATED
    else:
        return BAD_MAGICIAN


if __name__ == '__main__':

    T = int(raw_input())
    for t in xrange(T):
        answers = []
        arrangements = [[], []]
        
        # Read one case of input.
        answers.append(int(raw_input()))
        for i in xrange(4):
            arrangements[0].append(map(int,raw_input().split()))
        answers.append(int(raw_input()))
        for i in xrange(4):
            arrangements[1].append(map(int,raw_input().split()))

        print "Case #%d: %s" % (t+1, solve(answers, arrangements))

