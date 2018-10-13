def war_score(l, blocks_naomi, blocks_ken):
    score_naomi = 0
    last_checked = 0
    for i, block_naomi in enumerate(blocks_naomi):
        if last_checked < l:
            j = last_checked
            for k, block_ken in enumerate(blocks_ken[j:]):
                if block_ken < block_naomi:
                    score_naomi += 1
                    last_checked = last_checked + 1
                else:
                    last_checked = last_checked + 1
                    break
    return score_naomi


def deceitful_war_score(l, blocks_naomi, blocks_ken):
    score_naomi = 0
    if l == 1:
        if blocks_naomi[0] > blocks_ken[0]:
            score_naomi += 1
    else:
        if blocks_naomi[0] > blocks_ken[0]:
            lnew = l -1
            bn = blocks_naomi[1:]
            bk = blocks_ken[1:]
            score_naomi = 1 + deceitful_war_score(lnew, bn, bk)
        else:
            lnew = l - 1
            bn = blocks_naomi[1:]
            bk = blocks_ken[:-1]
            score_naomi = deceitful_war_score(lnew, bn, bk)
    return score_naomi


data = open('deceitful_war.in').readlines()

num_tests = int(data[0].strip('\n'))

x = 1
for i in range(num_tests):
    l = int(data[x].strip('\n'))
    blocks_naomi = data[x+1].strip('\n').split()
    blocks_naomi.sort()
    blocks_ken = data[x+2].strip('\n').split()
    blocks_ken.sort()
    x = x + 3
    d_war_score = deceitful_war_score(l, blocks_naomi, blocks_ken)
    w_score = war_score(l, blocks_naomi, blocks_ken)
    print "Case #%s: %s %s" %(i+1, d_war_score, w_score)
    
