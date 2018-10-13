def solve_War(num, Naomi_blocks, Ken_blocks):
    Naomi = list(Naomi_blocks)
    Ken = list(Ken_blocks)

    if num == 1:
        if Naomi[0] > Ken[0]:
            return 1
        else:
            return 0
    win_cnt = 0

    while(len(Naomi) > 0):
        if Naomi[0] > Ken[len(Ken) - 1]:
            win_cnt += len(Naomi)
            return win_cnt
        if Ken[0] > Naomi[len(Naomi) - 1]:
            return win_cnt

        k_card = None
        for k in Ken:
            if k > Naomi[0]:
                k_card = k
                break
        if k_card:
            Ken.remove(k_card)
            Naomi.pop(0)
        else:
            Ken.pop(0)
            Naomi.pop(0)
            win_cnt += 1

    return win_cnt


def solve_DeceitfulWar(num, Naomi_blocks, Ken_blocks):
    Naomi = list(Naomi_blocks)
    Ken = list(Ken_blocks)

    if num == 1:
        if Naomi[0] > Ken[0]:
            return 1
        else:
            return 0

    win_cnt = 0

    while (len(Naomi) > 0):
        if Naomi[0] > Ken[len(Ken) - 1]:
            win_cnt += len(Naomi)
            return win_cnt
        if Ken[0] > Naomi[len(Naomi) - 1]:
            return win_cnt

        if Naomi[len(Naomi) - 1] > Ken[len(Ken) - 1]:
            Naomi.pop(len(Naomi) - 1)
            Ken.pop(len(Ken) - 1)
            win_cnt += 1
        else:
            Naomi.pop(0)
            Ken.pop(len(Ken) - 1)

    return win_cnt


f_in = open('D-large.in', 'r')
f_out = open('D-large.out', 'w')

# f_in = open('sample.in', 'r')
# f_out = open('sample.out', 'w')

is_first = True
cnt = 0
p_cnt = 1

for line in f_in:
    if is_first:
        T = int(line)
        is_first = False
        continue
    elif cnt == 0:
        num_of_blocks = int(line)
        cnt += 1
        continue
    elif cnt == 1:
        Naomi_blocks = line.split()
        for i in range(num_of_blocks):
            Naomi_blocks[i] = float(Naomi_blocks[i])
        Naomi_blocks.sort()
        cnt += 1
    elif cnt == 2:
        Ken_blocks = line.split()
        for i in range(num_of_blocks):
            Ken_blocks[i] = float(Ken_blocks[i])
        Ken_blocks.sort()

        ans_deceitfulwar = (
            solve_DeceitfulWar(num_of_blocks, Naomi_blocks, Ken_blocks))
        ans_war = solve_War(num_of_blocks, Naomi_blocks, Ken_blocks)

        if p_cnt != T:
            ans_str = 'Case #%d: %d %d\n' % (p_cnt, ans_deceitfulwar, ans_war)
            f_out.write(ans_str)
            p_cnt += 1
            cnt = 0
            continue
        else:
            ans_str = 'Case #%d: %d %d' % (p_cnt, ans_deceitfulwar, ans_war)
            f_out.write(ans_str)
            break

f_in.close()
f_out.close()
