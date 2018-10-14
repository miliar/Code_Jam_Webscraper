#!env python

def main(input_file='input.txt', output_file='output.txt'):
    fd = open(input_file)
    cases = int(fd.readline())
    output = open(output_file, 'w')

    for i in range(cases):
        S, K = fd.readline().split()
        response = spin(S, int(K))
        print response

        output.writelines('Case #%d: %s\n' % (i + 1, response))


def flip(S, i, K):
    response = S[:i]
    for s in S[i:i + K]:
        response += '-' if s == '+' else '+'
    response += S[K + i:]
    return response


def spin(S, K):
    the_goal = ''.join(['+' for i in S])
    flip_count = (len(S) - K) + 1
    flips = 0
    for i in range(flip_count):
        if S[i] == '+':
            continue

        S = flip(S, i, K)
        flips += 1

    if S == the_goal:
        return str(flips)

    return 'IMPOSSIBLE'

if __name__ == '__main__':
    main(input_file='A-large.in')
