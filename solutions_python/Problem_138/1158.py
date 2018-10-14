import sys

def Kens_choice(goal, weights):
    if max(weights) <= goal:
        return min(weights)
    else:
        mindiff = 1
        for weight in weights:
            if (weight - goal) > 0 and (weight - goal) < mindiff:
                best = weight
                mindiff = weight - goal
        return best

T = int(sys.stdin.readline())
for testcase in range(T):
    # per testcase
    N = int(sys.stdin.readline())
    Naomi = map(float, sys.stdin.readline().split())
    Ken = map(float, sys.stdin.readline().split())

    Naomi2 = sorted(Naomi)
    Ken2 = sorted(Ken)

    # fair game
    naomi_score = 0
    n = N
    while N > 0:
        tell = min(Naomi)
        Naomi.remove(tell)

        move = Kens_choice(tell, Ken)
        if move < tell:
            naomi_score += 1
        Ken.remove(move)
        N -= 1
    fair_score = naomi_score

    naomi_score = 0
    N = n
    while N > 0:
        if (min(Naomi2) < min(Ken2) or max(Naomi2) < max(Ken2)):
            tell = max(Ken2) - 0.00000001
            Naomi2.remove(min(Naomi2))
        else:
            tell = max(Ken2) + 0.00000001
            Naomi2.remove(min(Naomi2))
        move = Kens_choice(tell, Ken2)
        if move < tell:
            naomi_score += 1
        Ken2.remove(move)
        N -= 1


    result = str(naomi_score) + " " + str(fair_score)

    print "Case #" + str(testcase + 1) + ": " + result

