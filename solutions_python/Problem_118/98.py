import codejam

def is_fair_square(n):
    sn = str(n)
    return sn == sn[::-1]

# Generate all possible cases
current_round = ["11", "22"]
possibles = [1, 4, 9, 121, 484]
nlen = 0
while nlen <= 50:
    next_round = []

    for number in current_round:
        nlen = len(number)

        fhalf, shalf = number[:nlen / 2], number[nlen / 2:]

        if nlen % 2 == 0:
            for i in ['0', '1', '2']:
                n = "%s%s%s" % (fhalf, i, shalf)
                n2 = int(n) ** 2
                if is_fair_square(n2):
                    possibles.append(n2)
                    next_round.append(n)

        else:
            n = "%s%s%s" % (fhalf, shalf[0], shalf)
            n2 = int(n) ** 2
            if is_fair_square(n2):
                possibles.append(n2)
                next_round.append(n)

    current_round = next_round

# Solve
for case in xrange(codejam.readint()):
    A, B = map(int, codejam.readstring().split())
    count = 0
    for possible in possibles:
        if A > possible:
            continue

        if B < possible:
            break

        count += 1

    print "Case #%d: %d" % (case + 1, count)
