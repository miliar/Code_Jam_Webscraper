import fileinput

def flip_with_flipper(S, k, index):
    for i in xrange(k):
        if S[index + i] == "-":
            S[index + i] = "+"
        else:
            S[index + i] = "-"

def solve(S, k):
    flips = 0

    last_available_flip = len(S) - k + 1

    for i in range(0, last_available_flip):
        if S[i] == "-":
            flip_with_flipper(S, k, i)
            flips += 1

    while i < len(S):
        if S[i] == "-":
            return "IMPOSSIBLE"

        i += 1

    return flips

if __name__ == "__main__":
    f = fileinput.input()

    T = int(f.readline()) # Number of cases
    for case in xrange(1, T + 1):
        S,k = f.readline().split(" ")
        S = list(S)
        k = int(k)
        solution = solve(S, k)
        print("Case #{0}: {1}".format(case, solution))