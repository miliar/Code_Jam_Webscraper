from __future__ import division

def min_expected_keystrokes(a, b, probs):
    # keep typing, enter right away, a different backspaces
    expected = [0 for i in range(a + 2)]

    curr_prob = 1
    for p in probs:
        curr_prob *= p

    # now curr_prob is P(all letters are typed correctly)
    update_expected(expected, a, b, curr_prob, wrong_pos=0)

    sum_of_prob = curr_prob

    # calc the same for all the possible wrong letters
    for wrong_pos in range(a, 0, -1):
        curr_prob = 1
        for p in probs[:wrong_pos - 1]:
            curr_prob *= p
        curr_prob *= 1 - probs[wrong_pos - 1]
        sum_of_prob += curr_prob
        update_expected(expected, a, b, curr_prob, wrong_pos)

    return min(expected)

def update_expected(expected, a, b, curr_prob, wrong_pos):
    # keep typing
    if wrong_pos == 0:  # no errors
        expected[0] += curr_prob * (b - a + 1)
    else:
        expected[0] += curr_prob * (b - a + 1 + b + 1)

    # enter right away
    expected[1] += curr_prob * (1 + b + 1)

    # up to a backspaces
    for j in range(1, a + 1):
        expected[1 + j] += curr_prob * (j * 2 + (b - a + 1))
        if wrong_pos != 0 and (a - j + 1) > wrong_pos:
            # we didn't reach bad char
            expected[1 + j] += curr_prob * (b + 1)

with open("A-small-attempt0.in") as f:
    t = int(f.readline())
    for i in range(t):
        a, b = [int(num) for num in f.readline().split()]
        probs = [float(num) for num in f.readline().split()]
        print "Case #%d: %f" % (i + 1, min_expected_keystrokes(a, b, probs))
