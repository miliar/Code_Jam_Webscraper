from pprint import pprint

BAD_MAGICIAN = "Bad magician!"
VOLUNTEER_CHEATED = "Volunteer cheated!"

def load_from_file(filename):
    out = []
    with open(filename, 'r') as f:
        for line in f:
            out.append(line[:-1])
    return out


def save_to_file(filename, savelist):
    with open(filename, 'w+') as f:
        for line in savelist:
            f.write(line)
            f.write('\n')

def solve(cases):
    res = None
    for card in cases[0]:
        if card in cases[1]:
            if res is None:
                res = card
            else:
                return BAD_MAGICIAN
    if res is None:
        return VOLUNTEER_CHEATED
    else:
        return res

def create_out_list(reslist):
    out = []
    for i in range(len(reslist)):
        out.append("Case #{}: {}".format(i+1, reslist[i]))
    return out

if __name__ == "__main__":
    rows = load_from_file("A-small-attempt0.in")
    test_cases = int(rows[0])
    cur = 1
    res = []
    for i in range(test_cases):
        cards = []
        for j in range(2):
            ans = int(rows[cur])
            cur += ans
            card_row = [int(x) for x in rows[cur].split(" ")]
            cur += 5 - ans
            cards.append(card_row)
        res.append(solve(cards))
    save_to_file("out.txt", create_out_list(res))
