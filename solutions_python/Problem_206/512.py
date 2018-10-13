import sys

def get_lines():
    return [line.rstrip('\n') for line in sys.stdin]

def get_time_to_dest(D, horse):
    [K, S] = horse
    distance = D - K
    return distance / S

assert get_time_to_dest(2525, [2400, 5]) == 25.0

def solve(D, N, horses):
    max_time = -1
    for index in range(0, N):
        time = get_time_to_dest(D, horses[index])
        max_time = max(max_time, time)
    return D / max_time

assert solve(2525, 1, [[2400, 5]]) == 101.0
assert solve(300, 2, [[120, 60], [60, 90]]) == 100.0
assert solve(100, 2, [[80, 100], [70, 10]]) == (100.0 / 3.0)

def main():
    lines = get_lines()
    nb_cases = int(lines.pop(0))

    for case in range(0, nb_cases):
        D, N = map(int, lines.pop(0).split(' '))
        horses = []
        for index in range(0, N):
            K, S = map(int, lines.pop(0).split(' '))
            horses.append([K, S])
        answer = solve(D, N, horses)
        print("Case #", (case + 1), ": ", answer, sep="")

main()
