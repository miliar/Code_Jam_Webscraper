#!/usr/bin/env python

# "--++" => "HH++" => "HH--" => "++--"
def flipped(s):
    return s.replace("-", "H").replace("+", "-").replace("H", "+")

def compute_next(p, flipper_size):
    states = set()
    all = []
    for i, c in enumerate(p):
        if c == "+": continue
        # print "{}th unhappy".format(i)
        for j in xrange(flipper_size):
            # k is where to start flipping flipper_size pancakes
            k = i - j
            if k < 0: continue
            if k + flipper_size > len(p): continue
            new_state = (
                p[:k] +
                flipped(p[k:k+flipper_size]) +
                p[k+flipper_size:])
            # print "new_state: " + new_state
            # all.append(new_state)
            states.add(new_state)
    # print "Next: {} -> ({})".format(p, ", ".join(all))
    for s in states:
        yield s

def how_many_flips(initial, size):
    states = [(0, initial)]
    seen = set()
    while len(states) > 0:
        (n, p) = states.pop(0)
        seen.add(p)
        # print p
        if p.count("+") == len(initial):
            return n
        else:
            for next in compute_next(p, size):
                if next in seen: continue
                states.append((n + 1, next))
    return "IMPOSSIBLE"

def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        pancakes, flipper_size = raw_input().split()
        result = how_many_flips(pancakes, int(flipper_size))
        print "Case #{}: {}".format(i, result)

if __name__ == "__main__":
    main()
