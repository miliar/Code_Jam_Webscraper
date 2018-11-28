import copy

f = open('A-small-attempt0.in', 'r')
outf = open('output1.txt', 'w')

T = int(f.readline())

def collapse(f_strs):
    total_clps = list()
    total_cnt = list()
    for f_str in f_strs:
        clps_chars = list()
        char_cnt = list()

        str_len = len(f_str)
        ind_pre = 0
        pre_c = f_str[ind_pre]
        ind_c = 0
        while ind_c < str_len:
            if f_str[ind_c] != pre_c:
                clps_chars.append(pre_c)
                char_cnt.append(ind_c - ind_pre)
                ind_pre = ind_c
                pre_c = f_str[ind_pre]
            ind_c += 1
        clps_chars.append(pre_c)
        char_cnt.append(ind_c - ind_pre)
        total_clps.append(clps_chars)
        total_cnt.append(char_cnt)
            
    return total_clps, total_cnt

def can_change(total_clps, total_cnt):
    clps_chars = set(map(lambda x: ''.join(x), total_clps))
    if len(clps_chars) > 1:
        return -1

    moves = 0
    dif_c_num = len(total_cnt[0])
    for i in range(dif_c_num):
        c_cnt = [x[i] for x in total_cnt]
        # if 1 in c_cnt:
        #     moves += sum([x - 1 for x in c_cnt])
        # else:
        center = float(sum(c_cnt)) / len(c_cnt)
        near_int = int(round(center))
        if abs(abs(near_int - center) - 0.5) < 0.00001:
            lower_int = near_int - 1
            tmp_low = 0
            tmp_high = 0
            for i_cnt in c_cnt:
                tmp_low += abs(i_cnt - lower_int)
                tmp_high += abs(i_cnt - near_int)
            moves += min(tmp_low, tmp_high)
        else:
            moves += sum([abs(x - near_int) for x in c_cnt])
    return moves
                

for test_ind in range(T):
    N = int(f.readline())
    f_strs = [f.readline() for i in range(N)]
    total_clps, total_cnt = collapse(f_strs)
    moves = can_change(total_clps, total_cnt)

    if moves >= 0:
        out_str = 'Case #' + str(test_ind + 1) + ': ' + str(moves) + '\n'
    else:
        out_str = 'Case #' + str(test_ind + 1) + ': Fegla Won\n'
    outf.write(out_str)
        
f.close()
outf.close()
