from functools import reduce
def count_flips(pancakes, flipper_size):
    sides = [p == '+' for p in pancakes]
    flip_count = 0
    for i in range(0, len(pancakes) - flipper_size + 1):
        if not sides[i]:
            flip_count += 1
            sides[i:i+flipper_size] = map(lambda x: not x, sides[i:i+flipper_size])
    flipped = reduce(lambda x, y: x and y, sides)
    if flipped:
        return flip_count
    else:
        return 'IMPOSSIBLE'
            

T = int(input())
for i in range(1, T+1):
     case = input().split()
     flips = count_flips(case[0], int(case[1]))
     print('Case #{0}: {1}'.format(i, flips))

