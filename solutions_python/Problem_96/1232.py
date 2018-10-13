from itertools import combinations_with_replacement

GOOGLERS_INDEX = 0
SURPRIZING_TRIPLETS_INDEX = 1
MINIMUM_BEST_RESULT_INDEX = 2
PLAYERS_TOTAL_POINTS_START_INDEX = 3

def get_scores(total_points, is_surprizing = False):
    start = total_points/3 -4
    start = start if start >= 0 else 0
    end = start + 8
    end = end if end <= 30 else 30
    combinations = combinations_with_replacement(xrange(start, end), 3)
    all = [i for i in combinations if sum(i) == total_points and max(i) - min(i) < (3 if is_surprizing else 2)]
    return all

def main(input_path, output_path):
    infile = open(input_path)
    outfile = open(output_path, 'wt')
    cases = int(infile.readline())
    for case_number in xrange(1, cases + 1):
        case = infile.readline()
        case = [int(i) for i in case.split()]
        googlers = case[GOOGLERS_INDEX]
        surprizing = case[SURPRIZING_TRIPLETS_INDEX]
        min_best_result = case[MINIMUM_BEST_RESULT_INDEX]
        players = case[PLAYERS_TOTAL_POINTS_START_INDEX:]
        players.sort(reverse=True)
        answer = 0
        for player in players:
            if min_best_result <= max([max(i) for i in get_scores(player)]):
                answer += 1
                continue
            if surprizing > 0 and min_best_result <= max([max(i) for i in get_scores(player, is_surprizing = True)]):
                answer += 1
                surprizing -= 1
        outfile.write("Case #%d: %d\n" % (case_number, answer))
    outfile.close()
    infile.close()
if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
    
