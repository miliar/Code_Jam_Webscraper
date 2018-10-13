import re

t = int(raw_input())
for i in xrange(1, t + 1):
    pancakes, k = raw_input().split(" ")
    pancakes = list(pancakes)
    k = int(k)

    flip_count = 0
    pancakes_len = len(pancakes)
    for pancake_index, pancake in enumerate(pancakes):
        if "-" not in pancakes:
            break
        if pancake == "-":
            if pancakes_len - k - pancake_index >= 0:
                flip_count += 1
                for _k in xrange(0, k):
                    if pancakes[pancake_index + _k] == "-":
                        pancakes[pancake_index + _k] = "+"
                    else:
                        pancakes[pancake_index + _k] = "-"
        # print pancakes

    if "-" in pancakes:
        flip_count = "IMPOSSIBLE"

    print "Case #{}: {}".format(i, str(flip_count))
