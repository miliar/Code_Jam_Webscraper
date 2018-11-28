def switch(S):
    for (i, c) in enumerate(S):
        # print(S)
        S[i] = op(S[i])
    # print(S)
    return S


def op(c):
    if c == '+':
        return '-'
    else:
        return '+'


def tri(S, K):
    pancakes = list(S)
    # print(pancakes)
    swapped = 0
    for i in range(len(pancakes)-K+1):
        c = pancakes[i]
        # print(i, " ", c, " ", pancakes)
        if c == '-':
            pancakes[i:i + K] = switch(pancakes[i:i+K])
            swapped += 1

    if set(pancakes) == set('+'):
        print(swapped)
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    f_input = open("A-large.in")
    t = int(f_input.readline())
    for test_number in range(0, t):
        (S, K) = str(f_input.readline()).split()
        print("Case #{}: ".format(test_number +1), end='')
        tri(S, int(K))
