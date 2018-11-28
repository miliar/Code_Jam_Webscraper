def ken_play(naomi_told, ken):
    if naomi_told > max(ken):
        return (True, min(ken))
    else:
        return (False, min(filter(lambda x: x > naomi_told, ken)))

def calc_war(naomi, ken):
    naomi_score = 0
    for i in naomi:
        k = ken_play(i, ken)
        ken.remove(k[1])
        naomi_score += 1 if k[0] else 0
    return naomi_score

def calc_dwar(naomi, ken):
    naomi_score = 0
    for i in range(len(naomi)):
        if min(ken) < min(naomi):
            naomi_told = max(ken) + .000001 #ken plays min
            naomi.remove(min(naomi)) #naomi plays min and wins
        else:
            naomi_told = max(ken) - .000001 #ken plays max
            naomi.remove(min(naomi)) #naomi plays min and loses
        k = ken_play(naomi_told, ken)
        ken.remove(k[1])
        naomi_score += 1 if k[0] else 0
    return naomi_score


if __name__ == "__main__":
    cases = int(input())
    for case in range(cases):
        num_blocks = int(input())
        naomi = list(map(float, input().split(' ')))
        ken = list(map(float, input().split(' ')))

        war = calc_war(naomi, ken[:])
        dwar = calc_dwar(naomi[:], ken[:])
        print("Case #{}: {} {}".format(case+1, dwar, war))
