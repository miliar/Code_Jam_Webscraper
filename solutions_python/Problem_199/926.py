import fileinput

def flip(s, init, num):
    rs = ""
    for n, c in enumerate(s):
        if n >= init and n < init+num:
            rs += "-" if c == "+"  else "+"
        else:
            rs += c
    return rs

def bfs(init_state, k):
    if "-" not in init_state:
        return 0
    states_checked = []
    states_checking = [(init_state, [])]
    while states_checking:
        curr_state = states_checking.pop(0)
        for i in range(len(init_state) - k + 1):
            new_state = (flip(curr_state[0], i, k), [curr_state[0]] + curr_state[1])
            if new_state[0] == "+" * len(init_state):
                return len(new_state[1])
            elif new_state[0] not in map(lambda x: x[0], states_checked) and new_state[0] not in map(lambda x: x[0], states_checking):
                states_checking.append(new_state)
        states_checked.append(curr_state)
    return "IMPOSSIBLE"


if __name__ == "__main__":
    for case, line in enumerate(fileinput.input()):
        if case == 0:
            continue
        state, k = line.strip().split()
        k = int(k)
        print("Case #{}: {}".format(case, bfs(state, k)))
