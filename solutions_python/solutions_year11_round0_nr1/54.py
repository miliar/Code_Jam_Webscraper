T = input()
for t in range(T):
    x = raw_input().split()[1:]
    ans = 0
    o_pos = 1
    b_pos = 1
    for i in range(0, len(x), 2):
        o_goal = -1
        b_goal = -1
        for j in range(i, len(x), 2):
            if o_goal == -1 and x[j] == 'O':
                o_goal = int(x[j+1])
            if b_goal == -1 and x[j] == 'B':
                b_goal = int(x[j+1])
        if x[i] == 'O':
            elapse = abs(o_goal - o_pos) + 1
            o_pos = o_goal
            ans += elapse
            if b_goal != -1:
                if elapse >= abs(b_goal - b_pos):
                    b_pos = b_goal
                else:
                    if b_goal > b_pos:
                        b_pos += elapse
                    else:
                        b_pos -= elapse
        elif x[i] == 'B':
            elapse = abs(b_goal - b_pos) + 1
            b_pos = b_goal
            ans += elapse
            if o_goal != -1:
                if elapse >= abs(o_goal - o_pos):
                    o_pos = o_goal
                else:
                    if o_goal > o_pos:
                        o_pos += elapse
                    else:
                        o_pos -= elapse
    print 'Case #%d: %d' % (t+1, ans)