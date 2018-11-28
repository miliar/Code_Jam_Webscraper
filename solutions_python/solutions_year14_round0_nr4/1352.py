__author__ = 'panmari'


answers = []
filename = 'D-large.in'

answers = []
import math

def play_war(naomis_blocks, kens_blocks):
    # play through war
    w_score_naomi = 0
    w_score_ken = 0
    while (len(naomis_blocks) > 0):
        n_block = naomis_blocks.pop()
        ken_scored = False
        for idx, b in enumerate(kens_blocks):
            if b > n_block:
                w_score_ken += 1
                ken_scored = True
                del(kens_blocks[idx])
                break
        if not ken_scored:
            del(kens_blocks[0])  # kill his smallest block
            w_score_naomi += 1

    return w_score_naomi

def play_deceitful_war(naomis_blocks, kens_blocks):
    # play through war
    score_naomi = 0
    score_ken = 0
    while len(naomis_blocks) > 0:
        if naomis_blocks[0] < kens_blocks[0]:  # get him to waste his cube!
            naomis_blocks.pop(0)
            kens_blocks.pop()
            score_ken += 1
        else:
            naomis_blocks.pop(0)
            kens_blocks.pop(0)
            score_naomi += 1
    return score_naomi

with open(filename) as file:
    nr_problems = file.readline()
    while True:
        nextLine = file.readline()
        if nextLine == '':
            break
        nr_blocks = int(nextLine)
        naomis_blocks_init = [float(x) for x in file.readline().split(' ')]
        naomis_blocks_init.sort()
        kens_blocks_init = [float(x) for x in file.readline().split(' ')]
        kens_blocks_init.sort()

        war_score_naomi = play_war(naomis_blocks_init[:],kens_blocks_init[:])

        d_war_score_naomi = play_deceitful_war(naomis_blocks_init[:], kens_blocks_init[:])

        answers.append('{} {}'.format(d_war_score_naomi, war_score_naomi))

with open(filename + '.out', 'w') as f:
    for n, answer in enumerate(answers):
        f.write("Case #{}: {}\n".format(n + 1, answer))