t = int(raw_input())


def flip(pancakes):
    def turn(pancake):
        if pancake == '-':
            return '+'
        else:
            return '-'
    return ''.join([turn(pancake) for pancake in pancakes])


def run(stove, k):
    left_pancake_index = 0
    right_pancake_index = len(stove) - 1
    flips = 0
    while left_pancake_index < right_pancake_index:
        if stove[left_pancake_index] == '-':
            stove = stove[:left_pancake_index] + \
                    flip(stove[left_pancake_index:left_pancake_index + k]) + \
                    stove[left_pancake_index + k:]
            flips += 1
        if stove[right_pancake_index] == '-':
            stove = stove[:right_pancake_index - (k - 1)] + \
                    flip(stove[right_pancake_index - (k - 1): right_pancake_index + 1]) + \
                    stove[right_pancake_index + 1:]
            flips += 1
        left_pancake_index += 1
        right_pancake_index -= 1

    return flips if '-' not in stove else 'IMPOSSIBLE'

if __name__ == '__main__':
    for i in xrange(1, t + 1):
        user_input = raw_input().split(" ")
        answer = run(user_input[0], int(user_input[1]))
        print 'Case #{}: {}'.format(i, answer)






