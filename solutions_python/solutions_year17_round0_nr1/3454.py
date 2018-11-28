T = int(input())

def get_min_flips(s, k):
    if '-' not in s:
        return 0
    if k > len(s):
        return "IMPOSSIBLE"
    if s[0] == '+':
        # recurse
        return get_min_flips(s[1:], k)
    else:
        # flip at beginning
        for i in range(k):
            s[i] = '+' if s[i] == '-' else '-'
        # recurse
        retval = get_min_flips(s[1:], k)
        return 1 + retval if retval != "IMPOSSIBLE" else "IMPOSSIBLE"


for t in range(T):
    line = input().split()
    pancakes_row = list(line[0])
    flipper_size = int(line[1])
    min_num_flips = get_min_flips(pancakes_row, flipper_size)
    print ("Case #" + str(t+1) + ": " + str(min_num_flips))
