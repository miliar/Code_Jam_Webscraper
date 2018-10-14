import sys

def input_to_state(input_state: str):
    return [(1 if c == '+' else (0 if c == '-' else -1)) for c in input_state]


def state_to_input(state):
    return ''.join([('+' if c == 1 else ('-' if c == 0 else 'X')) for c in state])


def flip(state, position: int, k: int):
    r = state.copy()

    for i in range(position, position + k):
        r[i] = int(not r[i])

    return r



def solve(state, k: int) -> int:
    length = len(state)
    #print('START STATE: ' + state_to_input(state))

    numFlips = 0

    for i in range(0, length - k + 1):
        if state[i] == 0:
            state = flip(state, i, k)
            numFlips += 1
            #print('STATE FLIPPED at ' + str(i) + ': ' + state_to_input(state))

    if 0 in state:
        return -1
    else:
        return numFlips


#################################
# Parse input and solve

def run():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    results = []
    with open(input_file, 'r') as f:
        numCases = int(f.readline())
        for i in range(0, numCases):
            caseStr = f.readline()
            state = input_to_state(caseStr.split(' ')[0])
            k = int(caseStr.split(' ')[1])

            result = solve(state, k)

            if result == -1:
                results.append('Case #{0}: IMPOSSIBLE\n'.format((i + 1)))
            else:
                results.append('Case #{0}: {1}\n'.format((i + 1), result))

    with open(output_file, 'w') as f:
        f.writelines(results)

if __name__ == '__main__':
    run()

