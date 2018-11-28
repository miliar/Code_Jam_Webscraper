def get_min_flip_number(pancakes, K):
    min_flip_number = 0
    while True:
        first_blank_idx = pancakes.find('-')
        if first_blank_idx == -1:
            return min_flip_number
        elif len(pancakes) - first_blank_idx < K:
            return -1
        else:
            flipped_pancakes = pancakes[first_blank_idx:first_blank_idx+K]
            flipped_pancakes = ''.join(['-' if pancake == '+' else '+' for pancake in flipped_pancakes])
            pancakes = pancakes[:first_blank_idx]+ flipped_pancakes + pancakes[first_blank_idx+K:]
            min_flip_number += 1

T = int(input())
for t in range(T):
    input_data = input().split()
    pancakes, K = input_data[0], int(input_data[1])

    min_flip_number = get_min_flip_number(pancakes, K)
    if min_flip_number > -1:
        print("Case #%d: %d" % (t+1, min_flip_number))
    else:
        print("Case #%d: IMPOSSIBLE" % (t+1))
