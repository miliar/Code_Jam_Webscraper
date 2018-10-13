import sys
sys.setrecursionlimit(9999999)

def oversized_pancake_flipper(filename):
    txt_file = open(filename, 'r')
    txt_file_result = open('A-large-result.txt', 'w')
    test_cases_amount = int(txt_file.readline().rstrip('\n'))

    for x in range(1, test_cases_amount + 1):
        test_info = txt_file.readline().rstrip('\n').split()
        actual_state = test_info[0]
        flipper_size = int(test_info[1])

        test_result = solve(actual_state, flipper_size, 0)
        test_result = test_result if test_result > -1 else 'IMPOSSIBLE'

        txt_file_result.write('Case #' + str(x) + ': ' + str(test_result) + '\n')

    txt_file_result.close
    txt_file.close

def flip(state):
    state = ''.join(state).replace('+', '%temp%').replace('-', '+').replace('%temp%', '-')
    return state

def solve(state, flipper_size, flip_amount):

    if state.count('-') == 0:
        return flip_amount

    index = state.index('-')

    if index + flipper_size > len(state):
        return -1

    state = ''.join(flip(list(state[index:index + flipper_size]))) + state[index + flipper_size:len(state)]

    return solve(state, flipper_size, flip_amount + 1)

oversized_pancake_flipper('A-large.in')