def solve(C, F, X):

    ncastles = 0
    current_time = 0
    current_score = 0

    while (current_score < X):
        current_production = ncastles * F + 2.0

        win = (X - current_score) / current_production
        time_until_next_castle = max((C - current_score) / current_production, 0)

        time_to_win_with_next_castle = time_until_next_castle + (X - (time_until_next_castle * current_production + current_score - C)) / (current_production + F)

        if (time_to_win_with_next_castle < win):
            current_time += time_until_next_castle
            current_score += time_until_next_castle * current_production
            current_score -= C
            ncastles += 1
        else:
            current_time += win
            current_score += win * current_production

    return current_time

def parse_input(filename='test.txt'):

    f = open(filename)
    lines = f.readlines()
    f.close()

    ncases = int(lines[0])

    casenum = 1

    for case in lines[1:]:
        C,F,X = map(float, case.split())
        print "Case #" + str(casenum) + ": " + str(solve(C,F,X))
        casenum += 1

if __name__ == "__main__":
    parse_input('B-large.in')