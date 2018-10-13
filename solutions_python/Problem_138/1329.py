def get_war_data(lines):
    count = int(lines[0])
    lines = lines[1:]
    data = []
    for i in xrange(count):
        data.extend([lines[i*3:(i+1)*3]])
    results = []
    for item in data:
        blocks = int(item[0])
        blocks_naomi = [float(i) for i in item[1].split(" ")]
        blocks_ken = [float(i) for i in item[2].split(" ")]
        results.extend([{"n": blocks, "naomi": blocks_naomi, "ken": blocks_ken}])
    return results


def play_deceitful_war(n, naomi_blocks, ken_blocks):
    naomi = list(naomi_blocks)
    ken = list(ken_blocks)
    naomi.sort()
    ken.sort(reverse=True)
    naomi_score = 0
    for i in xrange(n):
        j = 0
        chosen_naomi = naomi[j]
        if chosen_naomi > ken[-1]:
            chosen_ken = ken[-1]
        else:
            chosen_ken = ken[j]
        if chosen_naomi < chosen_ken:
            told_naomi = chosen_ken - 0.0000001
        else:
            naomi_score += 1
            chosen_ken = min(ken)
        del naomi[j]
        ken.remove(chosen_ken)
    return naomi_score


def play_war(n, naomi_blocks, ken_blocks):
    naomi = list(naomi_blocks)
    ken = list(ken_blocks)
    naomi.sort()
    ken.sort()
    naomi_score = 0
    for i in xrange(n):
        j = 0
        chosen_naomi = naomi[j]
        pottential_chosen_ken = [x for x in ken if x > naomi[j]]
        if pottential_chosen_ken:
            chosen_ken = min(pottential_chosen_ken)
        else:
            chosen_ken = min(ken)
        if chosen_naomi > chosen_ken:
            naomi_score += 1
        del naomi[j]
        ken.remove(chosen_ken)
    return naomi_score


if __name__ == '__main__':
    with open("D-large.in", "rb") as f:
        data = f.read()

    lines = data.split("\n")
    datasets = get_war_data(lines)
    results = []
    for i, game in enumerate(datasets):
        score_dw = play_deceitful_war(game["n"], game["naomi"], game["ken"])
        score_w = play_war(game["n"], game["naomi"], game["ken"])
        results.extend(["Case #{0}: {1} {2}".format(i+1, score_dw, score_w)])

    with open("pd_results.in", "wb") as f:
        f.write("\n".join(results))
