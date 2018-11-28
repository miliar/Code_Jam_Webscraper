import sys

GUESS_STEP = 100

f_in = open("B-large.in", "r")
#f_in = open("B-small-attempt0.in", "r")
#f_in = open("cookies.in", "r")
f_out = open("cookies.out", "w")

size = int(f_in.readline())

def cost(C, F, X, n):
    cost = float(X) / (2 + n * F)
    for i in range(n):
        cost += float(C) / (2 + i * F)

    return cost

def estimate_max_n(C, F, X):
    return 100

for case_num in range(size):
    print "case: " + str(case_num + 1)
    data = [float(x) for x in f_in.readline().strip().split()]
    C = data[0]
    F = data[1]
    X = data[2]

    min_guess = 0
    max_guess = estimate_max_n(C, F, X)
    while True:
        if cost(C, F, X, max_guess) < cost(C, F, X, max_guess - 1):
            min_guess = max_guess
            max_guess *= 2
        else:
            break

    # the minimum is somewhere between min_guess and max_guess, bisect to find it

    guess = min_guess + (max_guess - min_guess) / 2
    while True:
        cost_guess = cost(C, F, X, guess)

        if guess == 0:
            minimum_cost = cost_guess
            break

        cost_left = cost(C, F, X, guess - 1)

        if cost_left > cost_guess:
            cost_right = cost(C, F, X, guess + 1)

            if cost_right > cost_guess:
                minimum_cost = cost_guess # found it, both neighbours are higher
                break
            else:
                min_guess = guess
                guess = guess + (max_guess - guess) / 2 # solution is to the right
        else:
            max_guess = guess
            guess = min_guess + (guess - min_guess) / 2 # solution is to the left

    f_out.write("Case #" + str(case_num + 1) + ": " + str(minimum_cost) + "\n")

f_in.close()
f_out.close()