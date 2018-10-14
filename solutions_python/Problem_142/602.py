
def match(target, test, i, score):
    try:
        while target[i] == test[i]:
            i += 1
    except Exception:
        if len(test) == len(target):
            return score
        elif len(test) < len(target):

            while len(test) < i and test[i-1] == test[i]:
                score += 1
                test = test[0:i] + test[i] + test[i:]
            if test[i-1] == target[i-1] and len(test) == len(target):
                return score
            return float("inf")

            return score + (len(target) - len(test))
        else:
            while len(test) > i and test[i-1] == test[i]:
                score += 1
                test = test[0:i-1] + test[i:]
            if test[i-1] == target[i-1] and len(test) == len(target):
                return score
            return float("inf")


    if target[i] != test[i]:
        new_score = float("inf")
        new_score2 = float("inf")

        if i > 0 and test[i-1] == target[i]:
            test2 = test[0:i] + target[i] + test[i:]
            new_score = match(target, test2, i, score+1)

        if i > 0 and test[i-1] == test[i]:
            test2 = test[0:i-1] + test[i:]
            new_score2 = match(target, test2, i, score+1)

        result = min(new_score, new_score2)
        return result




def calc(names):
    #print names
    return min( match(names[0], names[1], 0, 0), match(names[1], names[0], 0, 0))


#with open('sample1.in') as f:
with open('A-small-attempt2.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        n = int(f.readline())
        names = []
        for i in range(0, n):
            names.append(f.readline().strip())

        ans = calc(names)
        if ans != float("inf"):
            print('Case #%s: %s'%(str(puzzle_count + 1), str(ans)))
        else:
            print('Case #%s: Fegla Won'%(str(puzzle_count + 1)))
