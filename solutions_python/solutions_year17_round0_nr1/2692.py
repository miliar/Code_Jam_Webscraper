def flip_pancakes(pancakes, K):
    for i in range(1, K+1):
        pancakes[-i] = -pancakes[-i]
    return pancakes

def no_moves(pancakes, K):
    no_pancakes = len(pancakes)
    no_moves = 0
    while no_pancakes >= K:
        if pancakes[-1] == -1:
            flip_pancakes(pancakes, K)
            no_moves = no_moves + 1
        pancakes = pancakes[:-1]
        no_pancakes = no_pancakes - 1
    if -1 in pancakes:
        return "IMPOSSIBLE"
    else:
        return no_moves

cases = int(input())
for t in range(1, cases + 1):
    pancakes_str, K_str = [s for s in input().split(' ')]
    pancakes_lst = []
    for sign in pancakes_str:
        if sign == '+':
            pancakes_lst.append(1)
        elif sign == '-':
            pancakes_lst.append(-1)
    K = int(K_str)
    count = no_moves(pancakes_lst, K)
    print('Case #{}: {}'.format(t, count))

