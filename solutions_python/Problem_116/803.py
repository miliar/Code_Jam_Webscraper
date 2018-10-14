
def run_game(count):
    vertical_sums = [0,0,0,0]
    horizontal_sums = [0,0,0,0]
    vertical_targets = [4,4,4,4]
    horizontal_targets = [4,4,4,4]
    forward_diagonal_sum = 0
    forward_diagonal_target = 4
    backward_diagonal_sum = 0
    backward_diagonal_target = 4
    row_complete = [True,True,True,True]

    for i in range(0,4):
        line = raw_input()
        for j in range(0, len(line)):
            if line[j] == 'X':
                vertical_sums[j] -= 1
                horizontal_sums[i] -= 1
                if i == j:
                    forward_diagonal_sum -= 1
                if i == 3 - j:
                    backward_diagonal_sum -= 1
            elif line[j] == 'O':
                vertical_sums[j] += 1
                horizontal_sums[i] += 1
                if i == j:
                    forward_diagonal_sum += 1
                if i == 3 - j:
                    backward_diagonal_sum += 1
            elif line[j] == 'T':
                vertical_targets[j] -= 1
                horizontal_targets[i] -= 1
                if i == j:
                    forward_diagonal_target -= 1
                if i == 3 - j:
                    backward_diagonal_target -= 1
            else:
                row_complete[i] = False
    game_complete = True
    for i in range(0,4):
        if abs(horizontal_sums[i]) == horizontal_targets[i]:
            if horizontal_sums[i] > 0:
                print "Case #{}: O won".format(count)
                return
            else:
                print "Case #{}: X won".format(count)
                return
        if abs(vertical_sums[i]) == vertical_targets[i]:
            if vertical_sums[i] > 0:
                print "Case #{}: O won".format(count)
                return
            else:
                print "Case #{}: X won".format(count)
                return
        if not row_complete[i]:
            game_complete = False
    if abs(forward_diagonal_sum) == forward_diagonal_target:
        if forward_diagonal_sum > 0:
            print "Case #{}: O won".format(count)
            return
        else:
            print "Case #{}: X won".format(count)
            return
    elif abs(backward_diagonal_sum) == backward_diagonal_target:
        if backward_diagonal_sum > 0:
            print "Case #{}: O won".format(count)
            return
        else:
            print "Case #{}: X won".format(count)
            return
    if game_complete:
        print "Case #{}: Draw".format(count)
        return
    else:
        print "Case #{}: Game has not completed".format(count)

count = input()
for i in range(1, count):
    run_game(i)
    raw_input()
run_game(count)
