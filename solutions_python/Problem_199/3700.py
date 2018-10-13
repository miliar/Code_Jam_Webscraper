numOfProblem = input()


def flip(state, position, size):
    print position
    print size

    return state


def isHappy(state):
    return state.count('+') == len(state)


def CharToBin(char):
    return 1 if (char == '+') else 0


for i in range(0, numOfProblem, 1):
    pancakeState, flipper = raw_input().split()

    b = map(CharToBin, list(pancakeState))
    flipper = int(flipper)

    count = 0
    for j in range(len(b) - 1, flipper - 2, -1):

        if (b[j] == 0):
            count = count + 1
            for k in range(0, flipper, 1):
                b[j - k] = 1 - b[j - k]

    count = str(count)
    if sum(b) != len(b):
        count = "IMPOSSIBLE"

    output = 'Case #' + str(i + 1) + ': ' + str(count)

    print output