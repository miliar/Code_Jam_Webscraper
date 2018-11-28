import random
import bisect

with open('D-small-attempt0.in', 'r') as f:
    content = f.readlines()

content = [x.replace("\n", "") for x in content]

test_cases = []

T = int(content[0])
for i in range(T):
    case = {}
    case['N'] = int(content[3 * i + 1])
    case['naomi'] = [float(x) for x in content[3 * i + 2].split(" ")]
    case['ken'] = [float(x) for x in content[3 * i + 3].split(" ")]
    test_cases.append(case)


def pick_least_greater(chosen_naomi, blocks):
    try:
        return min(x for x in blocks if x > chosen_naomi)
    except:
        return max(x for x in blocks if x < chosen_naomi)


def pick_most_smaller(chosen_naomi, blocks):
    try:
        return max(x for x in blocks if x < chosen_naomi)
    except:
        return min(x for x in blocks if x > chosen_naomi)


def war(naomi, ken):
    num_blocks = len(naomi)
    ken_score = 0
    naomi_score = 0
    naomi = sorted(naomi)
    ken = sorted(ken)
    while num_blocks > 0:
        chosen_naomi = min(naomi)
        kens_pick = pick_least_greater(chosen_naomi, ken)
        if (chosen_naomi > kens_pick):
            naomi_score += 1
        else:
            ken_score += 1
        naomi.remove(chosen_naomi)
        ken.remove(kens_pick)
        num_blocks -= 1
    return [naomi_score, ken_score]


def deceitful_war(naomi, ken):
    num_blocks = len(naomi)
    ken_score = 0
    naomi_score = 0
    naomi = sorted(naomi)
    ken = sorted(ken)
    while num_blocks > 0:
        maxk = max(ken)
        maxn = max(naomi)
        told_naomi = min([maxk, maxn]) - 0.000001
        kens_pick = pick_least_greater(told_naomi, ken)
        chosen_naomi = min(naomi) if not all(maxn > x for x in ken) else maxn
        if (chosen_naomi > kens_pick):
            naomi_score += 1
        else:
            ken_score += 1
        naomi.remove(chosen_naomi)
        ken.remove(kens_pick)
        num_blocks -= 1
    return [naomi_score, ken_score]

for idx, case in enumerate(test_cases):
    war_val = war(case['naomi'], case['ken'])
    dwar_val = deceitful_war(case['naomi'], case['ken'])
    print "Case #%s: %s %s" % (idx + 1, dwar_val[0], war_val[0])
