# Final state - 0

def parse(string):
    result = 0
    for char in string:
        result <<= 1
        result += 1 if char == '-' else 0
    return result


def flip(state, pos, k):
    mask = ((1 << k) - 1) << pos
    return ((state ^ mask) & mask) | (state & ~mask)


def bfs(l, state, k):
    visited, queue = set(), [(state, 0)]
    while queue:
        current, d = queue.pop(0)
        if d > l - k + 1:
            return -1
        if current == 0:
            return d

        if current not in visited:
            for pos in range(l-k+1):
                next_state = flip(current, pos, k)
                if next_state < current:
                    queue.append((next_state, d+ 1))
    return -1

def solve_case():
    input_string, k = input().split(' ')
    k = int(k)
    l = len(input_string)

    start_state = parse(input_string)
    if not start_state:
        return 0
    return bfs(l, start_state, k)


# s = parse('---+-++-')
# print(s)
# print(bin(s))
# for pos in range(8 - 3 + 1):
#     print(bin(flip(s, pos, 3)))
# exit()


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        d = solve_case()
        print('Case #{}: '.format(i + 1), end='')
        if d == -1:
            print('IMPOSSIBLE')
        else:
            print(d)
