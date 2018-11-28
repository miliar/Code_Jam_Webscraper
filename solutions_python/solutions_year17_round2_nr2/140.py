import sys
import operator


def is_valid2(cycle):
    new_cycle = cycle[:]
    new_cycle.append(cycle[0])
    for first, second in zip(new_cycle[:-1], new_cycle[1:]):
        assert first != 0
        assert second != 0
        if first == second:
            return False

    return True


def is_valid(cycle, init_state):

    for k, val in init_state.items():
        if cycle.count(k) != val:
            return False
    new_cycle = list(cycle[:])
    new_cycle.append(cycle[0])

    good_pairs = [('O', 'B'), ('G', 'R'), ('V', 'Y'), ('R', 'Y'), ('Y', 'B'), ('B', 'R')]

    for first, second in zip(new_cycle[:-1], new_cycle[1:]):
        if first == second:
            return False

        if (first, second) not in good_pairs and (second, first) not in good_pairs:
            return False

    return True


def solve_basic(R, Y, B):
    N = R + Y + B
    state = {'R': R, 'Y': Y, 'B': B}
    init_state = state.copy()

    solution = [0] * N

    max_key = max(state.iteritems(), key=operator.itemgetter(1))[0]
    max_val = state[max_key]

    del state[max_key]

    if 2 * max_val > N:
        return 'IMPOSSIBLE'

    for i in range(max_val):
        solution[2*i] = max_key

    keys = state.keys()
    if state[keys[1]] == 0:
        keys = keys[::-1]
    for j in range(2*max_val-1, N):
        cur_key = keys[j % 2]
        solution[j] = cur_key
        state[cur_key] -= 1


    for i in range(N):
        if solution[i] == 0:
            cur_max_key = max(state.iteritems(), key=operator.itemgetter(1))[0]
            solution[i] = cur_max_key
            state[cur_max_key] -= 1

    if is_valid(solution, init_state) and is_valid2(solution):
        return ''.join(solution)
    else:
        raise ValueError('Invalid sol')


def alt_string(first_letter, second_letter, rep):

    res = ''.join([first_letter] + [second_letter, first_letter]*(rep))
    return res


def answer(N, R, O, Y, G, B, V):
    assert N == R + O + Y + G + B + V

    init_state = {'R': R, 'Y': Y, 'B': B, 'O': O, 'G': G, 'V': V}
    if N == R + Y + B:
        return solve_basic(R, Y, B)
    else:
        if O == B and O + B == N:
            return ''.join(['OB'] * O)

        if G == R and G + R == N:
            return ''.join(['GR'] * G)

        if V == Y and V + Y == N:
            return ''.join(['VY'] * V)

        if (O >= B and O > 0) or (G >= R and G > 0) or (V >= Y and V > 0):
            return 'IMPOSSIBLE'

        basic_sol = solve_basic(R-G, Y-V, B-O)
        if basic_sol == 'IMPOSSIBLE':
            return basic_sol


        new_sol = basic_sol[:]
        if G > 0:
            new_sol = new_sol.replace('R', alt_string('R', 'G', G), 1)
        if O > 0:
            new_sol = new_sol.replace('B', alt_string('B', 'O', O), 1)
        if V > 0:
            new_sol = new_sol.replace('Y', alt_string('Y', 'V', V), 1)


        if not is_valid(new_sol, init_state):
            raise ValueError('fucked up')

        return new_sol

if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        queries.append(map(int, (sys.stdin.next()).split(' ')))
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i+1), ": ", str(answer(*q))])

