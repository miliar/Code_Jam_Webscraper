import sys


def war(naomi, ken):
    score = 0
    for _ in range(len(naomi)):
        chosen_naomi = max(naomi)
        max_ken = max(ken)
        if max_ken > chosen_naomi:
            chosen_ken = max_ken
        else:
            chosen_ken = min(ken)
            score += 1
        naomi.discard(chosen_naomi)
        ken.discard(chosen_ken)

    return score


def deceitful_war(naomi, ken):
    score = 0
    for _ in range(len(naomi)):
        chosen_ken = max(ken)
        if max(naomi) > max(ken):
            chosen_naomi = max(naomi)
            score += 1
        else:
            chosen_naomi = min(naomi)
        naomi.discard(chosen_naomi)
        ken.discard(chosen_ken)

    return score


def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    for case in range(int(lines[0])):
        naomi = {float(x) for x in lines[case * 3 + 2].split()}
        ken = {float(x) for x in lines[case * 3 + 3].split()}
        print('Case #{}: {} {}'.format(
            case + 1,
            deceitful_war(naomi.copy(), ken.copy()),
            war(naomi, ken))
        )

if __name__ == '__main__':
    main()
