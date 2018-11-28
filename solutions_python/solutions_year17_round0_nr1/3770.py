import sys

name = "test"
path = ""

testCases = int(input())

def flip( state ):
    if state == '-':
        state = '+'
    elif state == '+':
        state = '-'
    else:
        print("flip Error! Input not expected", state, file=sys.stderr)
    return state

for testCase in range(1, (testCases + 1)):
    line = input().split()
    S = list(line[0])   # the sequence of this line into array
    K = int(line[1])    # the flipper size

    count = 0

    for i in range(0, (len(S) - K + 1)):
        if S[i] == '-':
            for j in range(K):
                S[i + j] = flip(S[i + j])   # flipping every thing covered
                                            # within range K
            count = count + 1               # update counter

    for i in range((len(S) - K), len(S)):
        if S[i] == '-':
            count = 'IMPOSSIBLE'

    print("Case #" + str(testCase) + ": " + str(count))    # Grand result
