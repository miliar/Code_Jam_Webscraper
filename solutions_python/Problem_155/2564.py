
def solve(s_list):
    current_s = 0
    requiered_s = 0
    invited_f = 0
    for s in s_list:
        if requiered_s > current_s:
            invited_f += requiered_s - current_s
            current_s = requiered_s

        current_s += s
        requiered_s += 1

    return invited_f


def solve_all(in_, out):
    num_cases = int(in_.readline())
    for case in range(num_cases):
        _, ss = in_.readline().split()
        s_list = map(int, ss)
        num_friends = solve(s_list)
        out.write("Case #{}: {}\n".format(case + 1, num_friends))


def main():
    with open("A-large.in") as in_:
        with open("output.txt", 'w') as out:
            solve_all(in_, out)


if __name__ == "__main__":
    main()
