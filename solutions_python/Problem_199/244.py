def find_i(state, k, prev_i):
    i = prev_i
    while i < len(state):
        if state[i] is False:
            break
        i += 1
    return i


def flippable(state, k, i):
    if i >= len(state) or state[i] is True:
        return False
    return i <= len(state) - k


def flip(state, k, i):
    # print('Flipping {} at {}'.format(state, i))
    for j in range(i, i + k):
        state[j] = not state[j]

num_tests = int(input())
for test in range(1, num_tests + 1):
    line = input().split(' ')
    state_str, k = line[0], int(line[1])
    state = [c == '+' for c in state_str]

    flips = 0
    i = find_i(state, k, 0)
    # print('First i: {}'.format(i))
    while flippable(state, k, i):
        flip(state, k, i)
        flips += 1
        i = find_i(state, k, i)
        # print('Next i: {}'.format(i))
    # print(state)

    if all(state):
        print('Case #{}: {}'.format(test, flips))
    else:
        print('Case #{}: IMPOSSIBLE'.format(test))
