# check if each pancake is happy
def is_all_happy(state):
    for node in state:
        if node != 1:
            return False
    return True

# transform +,- to 1, -1
def transform(character):
    if character == '+':
        return 1
    else:
        return -1

# flip one pancake
def flip(state, i):
    state[i] *= -1

# find min number of flips
# return "IMPOSSIBLE" if cook can't make all pancake happy
# Otherwise, return min number of flips
def get_min_flips(state, k):
    if is_all_happy(state):
        return 0
    l = len(state)
    if k > l:
        return "IMPOSSIBLE"
    i = 0
    num_flip = 0
    while i < l - k + 1:
        if state[i] == -1:
            for x in xrange(i, i + k):
                flip(state, x)
            num_flip += 1
        i += 1
    if is_all_happy(state):
        return num_flip
    else:
        return "IMPOSSIBLE"

# main
T = int(raw_input())
for i in xrange(1, T+1):
    line = raw_input().split(" ")
    state, k = map(transform, line[0]), int(line[1])
    result = get_min_flips(state, k)
    if result == "IMPOSSIBLE":
        print "Case #%d: %s" % (i, result)
    else:
        print "Case #%d: %d" % (i, result)
