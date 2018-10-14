T = int(input())

def solution(row, flip_size):
    # describe state
    flips = 0
    row_length = len(row)
    state = [True if ch=='+' else False for ch in row]
    states = set(str(state)) # store for infinite loop check
    # no need for flips
    if all(state):
        return flips
    # general solving
    l, r = state.index(False), row_length-1-state[::-1].index(False)
    # l, r = 0, row_length-1

    # while l+flip_size-1 <= r-flip_size+1: # no strict crossing
    while l < r:
        # print(l, r, state)

        if flips%2 == 0: # search and flip from left
            if l + flip_size - 1 <= row_length-1:
                state[l: l+flip_size] = [not val for val in state[l: l+flip_size]]
                flips += 1
            else:
                break
        else:
            if r-flip_size+1 >= 0:
                state[r-flip_size+1: r+1] = [not val for val in state[r-flip_size+1: r+1]]
                flips += 1
            else:
                break
        if str(state) not in states:
            states.add(str(state))
        else:
            break
        try:
            l, r = state.index(False), row_length-1-state[::-1].index(False)
        except ValueError:
            break
    if l == r:
        if flip_size == 1:
            flips += 1          
    if all(state):
        return flips
    return "IMPOSSIBLE"

for i in range(T):
    items = input().split(' ')
    row_i = items[0]
    flip_size_i = int(items[1])
    print("Case #{}: {}".format(i+1, solution(row_i, flip_size_i)))