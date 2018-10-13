import sys

NAME = 0
COUNT = 1

def get_lines():
    return [line.rstrip('\n') for line in sys.stdin]

def get_max_index(colors, exclude, prefer_color=None):
    max_count = 0
    max_index = -1
    for index in range(0, len(colors)):
        color = colors[index]
        if color[NAME] in exclude:
            continue
        if max_count < color[COUNT]:
            max_count = color[COUNT]
            max_index = index
        elif max_count == color[COUNT] and prefer_color == color[NAME]:
            max_index = index
    return max_index

assert get_max_index([["R", 1], ["O", 0], ["Y", 2]], []) == 2
assert get_max_index([["R", 1], ["O", 10], ["Y", 2]], []) == 1
assert get_max_index([["R", 20], ["O", 10], ["Y", 2]], []) == 0
assert get_max_index([["R", 20], ["O", 10], ["Y", 2]], ["R"]) == 1
assert get_max_index([["R", 20], ["O", 10], ["Y", 0]], ["R", "O"]) == -1
assert get_max_index([["R", 2], ["O", 1], ["Y", 2]], [], "Y") == 2
assert get_max_index([["R", 2], ["O", 1], ["Y", 2]], ["Y"], "Y") == 0

def solve(N, colors):
    total = 0
    for color in colors:
        total += color[1]
    if total > N:
        return "IMPOSSIBLE"
    result = ""
    for index in range(0, N):
        exclude = []
        prefer = None
        if index > 0:
            exclude.append(result[index - 1])
        if (index + 1) == N:
            exclude.append(result[0])
        elif index > 0:
            prefer = result[0]
        max_index = get_max_index(colors, exclude, prefer)
        if max_index == -1:
            return "IMPOSSIBLE"
        result += colors[max_index][NAME]
        colors[max_index][COUNT] -= 1
    return result

def main():
    lines = get_lines()
    nb_cases = int(lines.pop(0))

    for case in range(0, nb_cases):
        N, R, O, Y, G, B, V = map(int, lines.pop(0).split(' '))
        colors = [
            ["R", R],
            ["O", O],
            ["Y", Y],
            ["G", G],
            ["B", B],
            ["V", V],
        ]
        answer = solve(N, colors)
        print("Case #", (case + 1), ": ", answer, sep="")

main()
