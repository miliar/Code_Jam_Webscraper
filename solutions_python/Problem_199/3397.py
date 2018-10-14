import copy

def check(state):
    for j in range(0, len(state)):
        if state[j] == '-':
            return False
    return True

def flip(state, start_point, K):
    for j in range(start_point, start_point + K):
        if state[j] == '-':
            state[j] = '+'
        else:
            state[j] = '-'
    return state

def breadth_search(state, K):
    next_states = [(state, 0)]
    checked = {}
    result = -1
    while len(next_states) > 0:
        current_state, flips = next_states.pop()
        for start_point in range(0, len(state) - K + 1):
            next_state = flip(copy.deepcopy(current_state), start_point, K)
            if ''.join(next_state) in checked:
                if checked[''.join(next_state)] > flips + 1:
                    checked[''.join(next_state)] = flips + 1
                    next_states = [x for x in next_states if x != (''.join(next_state), checked[''.join(next_state)])]
                    next_states.append((next_state, flips + 1))
                continue
            if check(next_state):
                if result < 0:
                    result = flips + 1
                else:
                    # print(next_state)
                    result = min(flips + 1, result)
            else:
                # print(next_state)
                checked[''.join(next_state)] = flips + 1
                next_states.append((next_state, flips + 1))
    if result < 0:
        return False
    else:
        return result

c_num = int(input())
cases = []
for i in range(0, c_num):
    cases.append(input())
for i in range(0, c_num):
    state, K = cases[i].split()
    K = int(K)
    # 14print(state, K)
    state = list(state)
    if check(state):
        print("Case #%d: 0" % (i + 1))
        continue
    f_result = breadth_search(state, K)
    if f_result:
        print("Case #%d: %d" % ((i + 1), f_result))
    else:
        print("Case #%d: IMPOSSIBLE" % (i + 1))
