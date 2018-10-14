def solve(ans1, ans2, card1, card2):
    ans = []

    for i in range(4):
        if card1[ans1-1][i] in card2[ans2-1]:
            ans.append(card1[ans1-1][i])

    if len(ans) == 0:
        return 'Volunteer cheated!'
    elif len(ans) == 1:
        return ans[0]
    else:
        return 'Bad magician!'

f_in = open('A-small-attempt0.in', 'r')
f_out = open('A-small-attempt0.out', 'w')

p_cnt = 1
is_first = True
cnt = 0
card1 = [[], [], [], []]
card2 = [[], [], [], []]

for line in f_in:
    if is_first:
        T = int(line)
        is_first = False
        continue
    else:
        if cnt == 0:
            ans1 = int(line)
            cnt += 1
            continue
        elif cnt <= 4:
            card1[cnt - 1] = line.split()
            cnt += 1
            continue
        elif cnt == 5:
            ans2 = int(line)
            cnt += 1
            continue
        elif cnt < 9:
            card2[cnt - 6] = line.split()
            cnt += 1
            continue
        elif cnt == 9:
            card2[3] = line.split()
            ans = solve(ans1, ans2, card1, card2)
            #print 'Case #%d: %s' % (p_cnt, ans)
            if p_cnt != T:
                f_out.write('Case #%d: %s\n' % (p_cnt, ans))
                p_cnt += 1
                cnt = 0
            else:
                f_out.write('Case #%d: %s' % (p_cnt, ans))
                break

f_in.close()
f_out.close()
