import fileinput

try:
    import psyco
    psyco.full()
except:
    pass

EPSILON = 0.0000001

def ken_war_strategy(naomi_card, kens_cards):
    if naomi_card > max(kens_cards):
        return min(kens_cards)
    return min([x for x in kens_cards if x > naomi_card])

def naomi_war_strategy(naomi_cards, kens_cards):
    ret_val = max(naomi_cards)
    return (ret_val, ret_val)

def naomi_deciteful_war_strategy(naomi_cards, kens_cards):
    naomi_max_card = max(naomi_cards)
    naomi_min_card = min(naomi_cards)
    kens_max_card = max(kens_cards)
    kens_min_card = min(kens_cards)
    if naomi_max_card > kens_min_card:
        return (kens_max_card + EPSILON, min([x for x in naomi_cards if x > kens_min_card]))
    return (kens_max_card - EPSILON, naomi_min_card)

def play_game(naomi, ken, naomi_strategy, kens_strategy ):
    naomi_score = 0
    while len(naomi) > 0:
        naomi_announced, naomi_real_val = naomi_strategy(naomi,ken)
        kens_move = kens_strategy(naomi_announced, ken)
        naomi.remove(naomi_real_val)
        ken.remove(kens_move)
        if naomi_real_val > kens_move:
            naomi_score += 1
            assert(naomi_announced > kens_move)
    return naomi_score

def solve_case(it):
    num_elements = int(it.next())
    naomi = [float(x) for x in it.next().split()]
    ken = [float(x) for x in it.next().split()]
    return (play_game(set(naomi),set(ken), naomi_deciteful_war_strategy, ken_war_strategy), play_game(set(naomi),set(ken), naomi_war_strategy, ken_war_strategy))


def main():
    it = fileinput.input()
    num_cases = int(it.next())
    for i in range(num_cases):
        solution = solve_case(it)
        print "Case #%d: %d %d" % (i+1,solution[0], solution[1])

if __name__ == "__main__":
    main()
