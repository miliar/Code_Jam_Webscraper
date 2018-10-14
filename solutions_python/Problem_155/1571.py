f_in = open('A-large.in', 'r')
f_out = open('A-large.out', 'w')

T = 0
i = 0
for line in f_in:
    if T == 0:
        T = int(line)
        i +=1
        continue

    tmp = line.strip().split()
    S_max = int(tmp[0])
    shyness_lst = list(map(int, list(tmp[1])))

    cur_sum = 0
    y = 0
    for shy_lvl, num in enumerate(shyness_lst):
        if cur_sum < shy_lvl and num != 0:
            y += shy_lvl - cur_sum
            cur_sum += shy_lvl - cur_sum
        cur_sum += num

    f_out.write('Case #' + str(i) + ': ' + str(y) + '\n')

    i += 1

f_out.close()
f_in.close()
