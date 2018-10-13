t = int(raw_input())  # read a line with a single integer
for index in xrange(1, t + 1):
    flips = 0
    pancakes, K = raw_input().split(' ')
    K = int(K)
    pancake_list = list(pancakes)
    i = 0
    while (i <= len(pancake_list)-K):
        if (pancake_list[i] == '-'):
            flips += 1
            j = i
            while j < i+K:
                if (pancake_list[j] == '+'):
                    pancake_list[j] = '-'
                else:
                    pancake_list[j] = '+'
                j += 1
        i+=1

    solved = True
    for pancake in pancake_list:
        if pancake != '+':
            solved = False

    pancakes_flipped = ''.join(pancake_list)
    if solved:
        print 'Case #{}: {}'.format(index, flips)
    else:
        print 'Case #{}: {}'.format(index, 'IMPOSSIBLE')