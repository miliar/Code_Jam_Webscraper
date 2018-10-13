def debug(msg):
    #print(msg)
    pass

def empty_stalls(stalls):
    return (i for i in range(len(stalls)) if not stalls[i])

def stall_distances(n,k):
    if n == k:
        return 0, 0

    stalls = [1] + [0] * n + [1]
    debug("Stalls {0}".format(stalls))

    num_stalls = len(stalls)

    ls, rs = None, None

    for person in range(k):
        stall_scores = []

        for stall in empty_stalls(stalls):
            ls = stall - 1
            while ls >= 0 and stalls[ls] == 0:
                ls -= 1
            ls = (stall - 1) - ls

            rs = stall + 1
            while rs < num_stalls and stalls[rs] == 0:
                rs += 1
            rs = rs - (stall + 1)

            stall_scores.append((stall, min(ls,rs), max(ls,rs), ls, rs))

        stall_scores = sorted(stall_scores, key=lambda tup: (tup[1],tup[2]), reverse=True)
        #stall_scores = sorted(stall_scores, key=lambda tup: tup[2])
        #stall_scores = sorted(stall_scores, key=lambda tup: tup[1])
        #debug("Stall scores {0}".format(stall_scores))
        best_stall = stall_scores[0]

        stalls[best_stall[0]] = 1
        ls, rs = best_stall[3], best_stall[4]

        debug("person {0} best stall {1}".format(person, best_stall))
        debug("Stalls {0}".format(stalls))

    debug("stalls end {0}".format(stalls))
    return ls, rs


def stalls():
    t = int(input())
    for case in range(1, t + 1):
        line = input().split(' ')
        n, k = int(line[0]), int(line[1])

        ls, rs = stall_distances(n, k)
        print("Case #{0}: {1} {2}".format(case, max(ls, rs), min(ls, rs)))


if __name__ == '__main__':
    stalls()
