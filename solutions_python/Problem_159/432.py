def find_min_eaten(plates):
    min_eaten = 0
    for i in range(len(plates) - 1):
        min_eaten += max(0, plates[i] - plates[i + 1])

    min_speed = 0
    for i in range(len(plates) - 1):
        min_speed = max(min_speed, plates[i] - plates[i + 1])

    min2_eaten = 0
    for i in range(len(plates) - 1):
        min2_eaten += min(plates[i], min_speed)

    return min_eaten, min2_eaten

def solve(f_in, line):
    line = f_in.readline()

    res = find_min_eaten([int(x) for x in line.split()])

    return "{0} {1}".format(res[0], res[1])

def test_solution():
    assert find_min_eaten([10, 5, 15, 5]) == (15, 25)
    assert find_min_eaten([100, 100]) == (0, 0)
    assert find_min_eaten([81, 81, 81, 81, 81, 81, 81, 0]) == (81, 567)
    assert find_min_eaten([23, 90, 40, 0, 100, 9]) == (181, 244)

if __name__ == '__main__': 
    import fileinput

    with fileinput.input() as f_input:
        f_input.readline()
        for i, line in enumerate(f_input, 1):
            result = solve(f_input, line)
            print("Case #{}: {}".format(i, result))

