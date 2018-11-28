from sys import stdin, stdout

def solve_fair(naomi, ken):
    naomi = sorted(naomi)
    ken = sorted(ken)
    score = 0
    for a in naomi:
        finished = False
        for b in ken:
            if b > a:
                ken.remove(b)
                finished = True
                break
        if not finished:
            score += 1
            ken.pop(0)
    return score

def solve_deceitful(naomi, ken):
    naomi = sorted(naomi)
    ken = sorted(ken)
    # print("Naomi: {}".format(str(naomi)))
    # print("Ken: {}".format(str(ken)))
    score = 0
    while len(naomi) > 0:
        while len(naomi) > 0 and naomi[-1] > ken[-1]:
            naomi.pop()
            ken.pop()
            score += 1
        if len(naomi) == 0:
            break
        # naomi[-1] < ken[-1]
        naomi.pop(0)
        ken.pop()
    return score

def main():
    lines = stdin.readlines()

    t = int(lines[0])
    lines = lines[1:]

    for i in range(t):
        n = int(lines[0])
        lines = lines[1:]
        naomi = [float(s) for s in lines[0].split()]
        ken = [float(s) for s in lines[1].split()]
        print("Case #{}: {} {}".format(i + 1, solve_deceitful(naomi, ken), solve_fair(naomi, ken)))
        lines = lines[2:]



main()
