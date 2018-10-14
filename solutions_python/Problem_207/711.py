import fileinput


# Solve problem

def has_different_hair_color(stalls):
    if len(stalls) is 1:
        return True

    first_color = stalls[0]
    last_color = stalls[-1]

    if first_color is "R":
        return last_color is "B" or last_color is "Y" or last_color is "G"
    if first_color is "O":
        return last_color is "B"
    if first_color is "Y":
        return last_color is "B" or last_color is "R" or last_color is "V"
    if first_color is "G":
        return last_color is "R"
    if first_color is "B":
        return last_color is "R" or last_color is "Y" or last_color is "O"
    if first_color is "V":
        return last_color is "Y"


def get_furthest_color(color, colors):
    if color is "R":
        if colors["G"] > 0:
            return "G"
        if colors["Y"] > colors["B"]:
            return "Y"
        if colors["B"] > 0:
            return "B"
        return False
    if color is "Y":
        if colors["V"] > 0:
            return "V"
        if colors["R"] > colors["B"]:
            return "R"
        if colors["B"] > 0:
            return "B"
        return False
    if color is "B":
        if colors["O"] > 0:
            return "O"
        if colors["Y"] > colors["R"]:
            return "Y"
        if colors["R"] > 0:
            return "R"
        return False
    if color is "O":
        if colors["B"] > 0:
            return "B"
        return False
    if color is "G":
        if colors["R"] > 0:
            return "R"
        return False
    if color is "V":
        if colors["Y"] > 0:
            return "Y"
        return False


def solve_problem(n, colors):
    stalls = []
    while n > 0:
        if len(stalls) is 0:
            for color in colors.keys():
                if colors[color] is not 0:
                    stalls.append(color)
                    colors[color] -= 1
                    n -= 1
                    break

        color = get_furthest_color(stalls[-1], colors)
        if color:
            stalls.append(color)
            colors[color] -= 1
            n -= 1
        else:
            return "IMPOSSIBLE"

    if has_different_hair_color(stalls):
        return "".join(stalls)
    else:
        return "IMPOSSIBLE"


# Utils


def parse_problem(case):
    [n, r, o, y, g, b, v] = case.split(' ')
    colors = dict()
    colors["R"] = int(r)
    colors["O"] = int(o)
    colors["Y"] = int(y)
    colors["G"] = int(g)
    colors["B"] = int(b)
    colors["V"] = int(v)
    return [int(n), colors]


def solve_case(case, case_number):
    [n, colors] = parse_problem(case)
    solution = solve_problem(n, colors)
    print("Case #" + str(case_number) + ": " + str(solution))


# Main script

def main():
    for index, line in enumerate(fileinput.input()):
        if index is 0:
            continue

        line = line.strip()
        solve_case(line, index)

if __name__ == "__main__":
    main()
