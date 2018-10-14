T = int(input())

for case_i in range(1, T+1):
    ans_str = "Case #" + str(case_i) + ': '

    line_inp = input().split()

    s_max = int(line_inp[0])
    
    invite_ans = 0
    cur_standup = 0
    list_s = [ int(s) for s in line_inp[1] ]

    for s_i, stand_si in enumerate(list_s):
        if s_i != 0:
            if cur_standup < s_i:
                # need to invite more
                invite_ans += s_i - cur_standup
                cur_standup += s_i - cur_standup
        cur_standup += stand_si

    ans_str += str(invite_ans)


    print(''.join([i if ord(i) < 128 else ' ' for i in ans_str]))
    #print(ans_str)


    #print('\n')



