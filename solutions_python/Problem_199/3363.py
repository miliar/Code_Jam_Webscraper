import os
import sys

def solve(state, K):
    num_steps = 0
    for i in range(len(state) - K + 1):
        if state[i] == 1:
            continue
        else:
            for j in range(i, i+K):
                state[j] = -1*state[j]
            num_steps += 1
    if sum(state[-K:]) == K:
        return num_steps
    return -1

if __name__ == '__main__':
    try:
        input = sys.argv[1]
    except:
        input = os.path.join('data', 'input.txt')
    output = os.path.join('data', 'output.txt')
    with open(input, 'r') as fin:
        with open(output, 'w') as fout:
            num_cases = int(fin.readline())
            for case in range(num_cases):
                fout.write('Case #%d: ' % (case+1))
                line = fin.readline().split(' ')
                state = list(map(lambda x: 1 if x == '+' else -1, line[0]))
                K = int(line[1])
                res = solve(state, K)
                if res >= 0:
                    fout.write(str(res) + '\n')
                else:
                    fout.write('IMPOSSIBLE\n')
