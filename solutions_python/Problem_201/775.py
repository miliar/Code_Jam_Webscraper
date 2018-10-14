
f = open('C-large.in', 'r').readlines()

T = int(f[0])

def getLR(size, cur_idx, step, goal):

    if size <= 1:
        return (0, 0)  # Base cases

    # Figure out the left and right sizes
    cur_L = (size // 2)
    cur_R = (size // 2)

    # If size is even, there is no middle stall so take one away from the left
    if size%2 == 0:
        cur_L -= 1

    # Check if we are at the goal
    if cur_idx == goal:
        return (cur_L, cur_R)

    # Figure out whether it's on the first or second side
    if (goal - (cur_idx+step))%(step*2) == 0:
        # It's on the first side, now to figure out whether the first is the left or right
        new_sz = cur_L if cur_L >= cur_R else cur_R
        return getLR(new_sz, cur_idx+step, step*2, goal)
    else:
        # It's on the second side
        new_sz = cur_R if cur_L >= cur_R else cur_L
        return getLR(new_sz, cur_idx+step*2, step*2, goal)



for t_case in xrange(1, T+1):
    # print('Processing test case #{}'.format(t_case))

    N, K = f[t_case].strip().split(' ')
    N = long(N)
    K = long(K)

    ret_LR = getLR(N, 1, 1, K)

    ret = (max(ret_LR), min(ret_LR))

    print('Case #{}: {} {}'.format(t_case, ret[0], ret[1]))

