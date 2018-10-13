fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

def war(naomi_blocks, ken_blocks):
    n = len(naomi_blocks)
    score = 0
    for j in range(n):
        block = naomi_blocks.pop(0)
        if block > ken_blocks[-1]:
            score += 1
            ken_blocks.pop(0)
        else:
            pick = 0
            while ken_blocks[pick] < block:
                pick += 1
            ken_blocks.pop(pick)
    return score

def deceitful_war(naomi_blocks, ken_blocks):
    n = len(naomi_blocks)
    score = 0
    for j in range(n):
        block = ken_blocks.pop(0)
        if block > naomi_blocks[-1]:
            naomi_blocks.pop(0)
        else:
            pick = 0
            score += 1
            while naomi_blocks[pick] < block:
                pick += 1
            naomi_blocks.pop(pick)
    return score

q = int(fin.readline())
for i in range(1, q + 1):
    n = int(fin.readline())
    true_score = 0
    false_score = 0
    naomi_blocks = sorted(list(map(float, fin.readline().split())))
    ken_blocks = sorted(list(map(float, fin.readline().split())))
    a = [naomi_blocks[i] for i in range(n)]
    b = [ken_blocks[i] for i in range(n)]
    true_score = war(a, b)
    false_score = deceitful_war(naomi_blocks, ken_blocks)
    print('Case #' + str(i) + ':', false_score, true_score, file = fout)

fin.close()
fout.close()
