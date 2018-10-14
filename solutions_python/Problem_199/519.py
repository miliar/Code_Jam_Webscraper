def flipper(sss):
    sflip = ''
    for s in sss:
        if s == '+':
            sflip += '-'
        else:
            sflip += '+'
    return sflip


def flip(state,flipper_size):

    idx = state.find('-')

    state = state[:idx] + flipper(state[idx:idx+flipper_size]) +state[idx+flipper_size:]

    return state

def answer(state,flipper_size):

    flip_times = 0

    while set(state) != {'+'}:

        if state.find('-') > len(state) - flipper_size:
            return 'IMPOSSIBLE'

        flip_times += 1
        state = flip(state,flipper_size)

    return flip_times


import sys

def main():

    with open(sys.argv[1]) as f:
        nums = int(f.readline())

        for i in range(nums):
            state,size = f.readline().strip().split()
            r = answer(state,int(size))
            print("Case #{:d}: ".format(i+1)+str(r))


main()
