import sys

# WARNING: Assumes all input is squeaky clean.

def main():
    T = int(sys.stdin.readline())

    for case_num in range(1,T+1):
        input_line = sys.stdin.readline()
        input_args = input_line.split(' ')
        S = list(input_args[0])
        K = int(input_args[1])

        y = 0
        leftmost = leftmost_index(S, '-')
        S_length = len(S)
        while -1 < leftmost <= S_length - K:
            flip(S, K, leftmost)
            leftmost = leftmost_index(S, '-')
            y += 1

        if '-' in S:
            y = "IMPOSSIBLE"

        print("Case #{0}: {1}".format(case_num, y))

def leftmost_index(sequence, elem):
    try:
        return sequence.index(elem)
    except:
        return -1

def flip(S, K, location):
    for i in range(location, location+K):
        if S[i] == '+':
            S[i] = '-'
        else:
            S[i] = '+'

if __name__ == "__main__":
    main()