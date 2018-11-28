import sys

INVALID = 0
NOTSURPRISING = 1
SURPRISING = 2


def score_total(score_tuple):
    return sum(score_tuple)


def categorize_score(score_tuple):
    a_b = abs(score_tuple[0] - score_tuple[1])
    a_c = abs(score_tuple[0] - score_tuple[2])
    b_c = abs(score_tuple[1] - score_tuple[2])

    if a_b > 2 or a_c > 2 or b_c > 2:
        return INVALID

    if a_b == 2 or a_c == 2 or b_c == 2:
        return SURPRISING

    return NOTSURPRISING


def guess_scores(total_score, surprising):
    base_score = total_score / 3

    difference = total_score - (base_score * 3)

    if base_score + difference > 10:
        return False, (base_score + 1, base_score + 1, base_score)
    else:
        if difference == 2:
            if surprising:
                return True, (base_score, base_score, base_score + 2)
            else:
                return False, (base_score + 1, base_score + 1, base_score)
        elif difference == 1:
            return False, (base_score + 1, base_score, base_score)
        elif difference == 0:
            if surprising:
                if base_score - 1 >= 0:
                    return True, (base_score-1, base_score, base_score+1)
                else:
                    return False, (base_score, base_score, base_score)
            else:
                return False, (base_score, base_score, base_score)


def main(num_googlers, num_surprising, min_score, *scores):
    actual_surprising = num_surprising
    guessed_scores = []

    for idx, input_score in enumerate(scores):
        if actual_surprising > 0:
            score = guess_scores(input_score, False)

            has_min = False

            for x in score[1]:
                if x >= min_score:
                    has_min = True
                    break

            #print has_min

            if not has_min:
                score = guess_scores(input_score, True)

                has_min = False

                for x in score[1]:
                    if x >= min_score:
                        has_min = True
                        break

                if not has_min:
                    score = guess_scores(input_score, False)
        else:
            score = guess_scores(input_score, False)

        #print input_score, score[0], score[1]

        if score[0]:
            actual_surprising -= 1

        guessed_scores.append(score[1])

    #assert actual_surprising == 0

    num_greater_equal = 0

    for score in guessed_scores:
        for x in score:
            if x >= min_score:
                num_greater_equal += 1
                break

    return num_greater_equal


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fd:
        fd.readline()

        for idx, line in enumerate(fd):
            line = line.strip()
            #print line
            print 'Case #%d: %d' % (idx + 1, main(*[int(x) for x in line.split(' ')]))
