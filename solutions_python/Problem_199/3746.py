import sys

def flip(p):
    if p == '+':
        return '-'
    elif p == '-':
        return '+'

t = int(input())

# Since flips commute, we can ignore the order of flips and build our solution left-to-right
# Furthermore, since any solution must place the first pancake in the correct orientation and
# only one possible flip affects the first position, we can proceed with a greedy algorithm.
for i in range(t):
    pancakes, flipper = input().split()
    flipper = int(flipper)
    pancakes = list(pancakes)
    flip_count = 0
    for p in range(len(pancakes)-(flipper-1)):
        if not pancakes[p] == '+':
            flip_count += 1
            for j in range(0,flipper):
                pancakes[p+j] = flip(pancakes[p+j])
    if set(pancakes)==set('+'):
        result = flip_count
    else:
        result = "IMPOSSIBLE"
    print("Case #{}: {}".format(i + 1, result))



