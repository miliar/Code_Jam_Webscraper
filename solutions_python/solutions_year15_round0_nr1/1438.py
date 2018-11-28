f = open('A-large.in', 'r')
outf = open('A-large-out.txt', 'w')

T = int(f.readline())

def friends_num(max_shy, audience):
    f_num = 0
    audience_part_sum = 0
    for i in range(1, max_shy + 1):
        audience_part_sum += audience[i - 1]
        if audience_part_sum < i:
            f_num += i - audience_part_sum
            audience_part_sum = i

    return f_num

for test_ind in range(T):
    seps = f.readline().split()
    max_shy = int(seps[0])
    audience = map(int, list(seps[1]))

    f_num = friends_num(max_shy, audience)

    out_str = 'Case #' + str(test_ind + 1) + ': ' + str(f_num) + '\n'
    outf.write(out_str)

f.close()
outf.close()
        
    
