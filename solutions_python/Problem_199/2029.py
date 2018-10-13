def debug(msg):
    #print(msg)
    pass

def check_solved(pancakes):
    solved = all("+" == pancake for pancake in pancakes)
    debug("{0} solved: {1}".format(pancakes, solved))
    return solved

def find_and_flip(pancakes, k):
    pancakes = list(pancakes)
    if "-" not in pancakes:
        debug("- not in pancakes")
        return tuple(pancakes)

    if k > len(pancakes):
        debug("k is > than len pancakes")
        return tuple(pancakes)

    # first negative pancake index
    fni = pancakes.index("-")

    # last index of flippable group ("-+-+-", k=3), should be 2
    lpi = len(pancakes) - k

    debug("fni {0} lni {1} len is {2}".format(fni, lpi, len(pancakes)))

    start_flip = fni if fni + k <= len(pancakes) else lpi
    for i in range(start_flip, start_flip + k):
        pancakes[i] = "+" if pancakes[i] == "-" else "-"
    debug("after flip {0}".format(pancakes))

    return tuple(pancakes)

def oversized_pancake():
    t = int(input())
    for case in range(1, t + 1):
        s, num = input().split(' ')

        pancakes = tuple([c for c in s])
        k = int(num)
        debug("input was: {0}, {1}".format(pancakes, k))

        #if (check_solved(pancakes)):
        #  debug("Case #{}: 0".format(case, 0))
        #  continue

        # Lame simulation
        soln = pancakes
        seen = set()
        seen.add(soln)
        number = 0
        while not check_solved(soln):
            soln = find_and_flip(soln, k)
            debug("step: {0}".format(soln))
            number += 1
            if soln in seen:
                print("Case #{}: IMPOSSIBLE".format(case))
                break
            seen.add(soln)

        else:
            print("Case #{0}: {1}".format(case, number))

if __name__ == '__main__':
    oversized_pancake()
