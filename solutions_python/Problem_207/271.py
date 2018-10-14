from sys import stdin, stdout, setrecursionlimit
from copy import deepcopy
setrecursionlimit(10000)

moves = {
   0: [1, 2, 4],
   1: [0, 2, 5],
   2: [0, 1, 3],
   3: [2],
   4: [0],
   5: [1],
}

to_char = "RYBOGV"

def solve(colour_counts):
    N, R, O, Y, G, B, V = colour_counts
    colours = {}
    for i, count in enumerate([R, Y, B, O, G, V]):
        colours[i] = count

    start = None
    for c in [3, 4, 5]:
        if colours[c] != 0:
            start = c
            break
    if not start:
        for c in [0, 1, 2]:
            if colours[c] != 0:
                start = c
                break
    placements = [start]
    colours[start] -= 1

    for _ in range(N-1):
        next_options = moves[placements[-1]]
        if len(next_options) == 1:
            next_option = next_options[0]
            if colours[next_option] == 0:
                return "IMPOSSIBLE"

        else:
            if colours[next_options[-1]] != 0:
                next_option = next_options[-1]
            else:
                cc1 = colours[next_options[0]]
                cc2 = colours[next_options[1]]
                if not cc1 and not cc2:
                    return "IMPOSSIBLE"

                if (cc1 == cc2):
                    if next_options[0] in moves[placements[0]]:
                        next_option = next_options[1]
                    else:
                        next_option = next_options[0]
                elif cc1 > cc2:
                    next_option = next_options[0]
                else:
                    next_option = next_options[1]

        placements.append(next_option)
        colours[next_option] -= 1

    if placements[-1] not in moves[placements[0]]:
        return "IMPOSSIBLE"

    return "".join(to_char[c] for c in placements)


T = int(stdin.readline())

for t in range(T):
    colour_counts = map(int, stdin.readline().strip().split())

    result = solve(colour_counts)

    stdout.write("Case #{}: {}\n".format(t+1, result))