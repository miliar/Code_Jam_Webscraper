import sys

def product(l):
    return reduce(lambda x,y:x*y, l, 1)

f = open(sys.argv[1])

t = int(f.readline())
for case in range(0, t):
    line = f.readline()
    a, b = map(int, line.split(" "))

    line = f.readline()
    ps = map(float, line.split(" "))

    best_expected_keystrokes = 2 + b

    success_prob = 1
    for i in range(a,-1,-1):
        #cost of i backspaces is 2i 1  + (b - a) + sometimes b + 1

        #probability that i backspaces will work is product of inverses
        #of probability that letters 0..i-1 are full of fail
        #success_prob = product(ps[:a-i])
        success_cost = 2 * i + 1 + (b - a)
        fail_cost = b + 2 * i + 2 + (b - a)
        fail_prob = 1 - success_prob


        expectation = success_prob * success_cost + fail_prob * fail_cost
        if expectation < best_expected_keystrokes:
            best_expected_keystrokes = expectation

        if i > 0:
            success_prob *= ps[a-i]

    print "Case #%d: %f" % (case+1, best_expected_keystrokes)
