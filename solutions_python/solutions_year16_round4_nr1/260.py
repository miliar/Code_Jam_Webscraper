game = {}
fight_table = [[-1] * 8 for y in xrange(8)]


def to_string(state):
    s = ""
    if state & 1:
        s += 'P'
    if state & 2:
        s += 'R'
    if state & 4:
        s += 'S'
    return state


def to_state(string):
    result = 0
    for c in string:
        if c == 'P':
            result += 1
        elif c == 'R':
            result += 2
        elif c == 'S':
            result += 4
    return result


def winner(a, b):
    if a == b:
        return ""
    if a > b:
        a, b = b, a

    if a == 'P' and b == 'R':
        return 'P'
    if a == 'P' and b == 'S':
        return 'S'
    if a == 'R' and b == 'S':
        return 'R'
    raise Exception()


def fight(state1, state2):
    if fight_table[state1][state2] != -1:
        return fight_table[state1][state2]
    s1 = to_string(state1)
    s2 = to_string(state2)
    result = set()
    for c1 in s1:
        for c2 in s2:
            result.add(winner(c1, c2))
    result.remove("")
    return to_state("".join(result))


def get_game(n, p, r, res):
    s = (1 << n) - p - r
    if s < 0:
        raise Exception()
    if (n, p, r, res) in game:
        return game[(n, p, r, res)]
    result = None
    if n == 0:
        if p == 1 and res == 'P':
            return 'P'
        elif r == 1 and res == 'R':
            return 'R'
        elif s == 1 and res == 'S':
            return 'S'
        else:
            return None
    n0 = n - 1
    for p0 in xrange(p, -1, -1):
        for r0 in xrange(r, -1, -1):
            s0 = (1 << n0) - p0 - r0
            if s0 < 0 or s0 > s:
                continue
            for left_res in 'PRS':
                for right_res in 'PRS':
                    if winner(left_res, right_res) == res:
                        first_result = get_game(n0, p0, r0, left_res)
                        second_result = get_game(n0, p - p0, r - r0, right_res)
                        if first_result is None or second_result is None:
                            continue
                        new_result = first_result + second_result
                        if result is None:
                            result = new_result
                        else:
                            result = min(result, new_result)
    game[(n, p, r, res)] = result
    return result


def solve(case_no):
    n, r, p, s = map(int, raw_input().split())
    answer = None
    for res in 'PRS':
        cur_game = get_game(n, p, r, res)
        if cur_game is not None:
            if answer is None:
                answer = cur_game
            else:
                answer = min(answer, cur_game)
    if answer is None:
        answer = "IMPOSSIBLE"
    print "Case #%d: %s" % (case_no, answer);


def main():
    T = int(raw_input())
    for case_no in xrange(1, T + 1):
        solve(case_no)


main()
