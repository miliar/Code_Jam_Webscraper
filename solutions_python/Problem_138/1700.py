# f_input = open('input.txt')
# f_input = open('D-small-attempt0.in')
f_input = open('D-large.in')
lines = f_input.read().split('\n')
f_input.close()

lines.pop(0)
lines.pop(len(lines) - 1)

def get_minimun_greater(weight, blocks):
    for i in range(len(blocks)):
        if blocks[i] > weight:
           return blocks.pop(i)
    return blocks.pop(0)

def get_war_scores(naomi_blocks, ken_blocks, N):
    naomi_scores = 0
    for i in range(N):
        naomi_block_weight = naomi_blocks.pop(0)
        minimun_greater = get_minimun_greater(naomi_block_weight, ken_blocks)
        if naomi_block_weight > minimun_greater:
            naomi_scores += 1
    return naomi_scores

def get_garbage_amount(min_weight, blocks):
    garbage_amount = 0
    for b in blocks:
        if b < min_weight:
            garbage_amount += 1
    return garbage_amount

def kill_giant_garbage(naomi_blocks, ken_blocks):
    naomi_blocks.pop(0)
    ken_blocks.pop()

def get_deceiful_war_scores(naomi_blocks, ken_blocks, N):
    naomi_scores = 0
    garbage_amount = get_garbage_amount(min(ken_blocks), naomi_blocks);
    while garbage_amount > 0:
        kill_giant_garbage(naomi_blocks, ken_blocks)
        garbage_amount -= 1
        N -= 1
    for i in range(N):
        ken_block_weight = ken_blocks.pop()
        minimun_greater = get_minimun_greater(ken_block_weight, naomi_blocks)
        if minimun_greater > ken_block_weight:
            naomi_scores += 1
    return naomi_scores

case = 0
all_result = ''
for i in range(0, len(lines), 3):
    case += 1
    result = 'Case #{}: {} {}\n'
    N = int(lines[i])
    naomi_blocks = sorted([float(b) for b in lines[i + 1].split(' ')])
    ken_blocks = sorted([float(b) for b in lines[i + 2].split(' ')])
    deceiful_war_score = get_deceiful_war_scores(naomi_blocks[:], ken_blocks[:], N)
    war_score = get_war_scores(naomi_blocks[:], ken_blocks[:], N)
    all_result += result.format(case, deceiful_war_score, war_score)
    print 'Case #%s' % (case)
    print naomi_blocks, ken_blocks
    print 'Deceiful War Score: ', deceiful_war_score
    print 'War Score: ', war_score

# f_output = open('output.txt', 'w')
f_output = open('output-large.txt', 'w')
f_output.write(all_result)
f_output.close()

