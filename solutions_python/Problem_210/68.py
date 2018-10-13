import sys
import operator


def greedy(prices, capacity):
    srt = sorted(prices)

    so_far_sum = 0
    for i in range(len(srt)):
        so_far_sum += srt[i]
        if so_far_sum > capacity:
            return i, capacity - so_far_sum - srt[i]
    return len(prices), capacity - so_far_sum


def solve_game(game_info, capacity):

    game_two = [item[0] for item in game_info if item[1] == 2]
    game_one = [item[0] for item in game_info if item[1] == 1]

    res1, capacity_left = greedy(game_two, capacity)
    res2, _ = greedy(game_one, capacity_left)
    return 2*res1 + res2


def answer(info):
    srt_info = sorted(info, key=lambda x: x[0])

    games = {'C': [], 'J': []}
    total_points = 0
    time_left = {'C': 720, 'J': 720}

    last = 'A'

    if srt_info[0][2] == srt_info[-1][2]:
        total_points += 2
        games[srt_info[0][2]].append((srt_info[0][0] + (1440 - srt_info[-1][1]), 2))
    else:
        total_points += 1


    last_end = 0
    for start, end, who in srt_info:
        time_left[who] -= end-start
        if last == 'A':
            last = who
            last_end = end
            continue
        else:
            if last == who:
                total_points += 2
                games[who].append(((start - last_end), 2))
            else:
                total_points += 1
        last_end = end
        last = who

    pts = sum([solve_game(games[key], time_left[key]) for key in ['C', 'J']])
    return total_points - pts




if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        Ac, Aj = map(int, sys.stdin.next().split(' '))
        info = []
        for j in range(Ac):
            start, end = map(int, sys.stdin.next().split(' '))
            info.append((start, end, 'C'))
        for j in range(Aj):
            start, end = map(int, sys.stdin.next().split(' '))
            info.append((start, end, 'J'))
        queries.append(info)
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i + 1), ": ", str(answer(q))])

