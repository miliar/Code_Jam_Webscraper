t = int(raw_input())

tests = []

for i in range(t):
    tests.append(raw_input().split())

output_file = "A-solution.out"


def minimumFlips(pancakes, k):
    moves = 0
    ps = list(pancakes)
    for i in range(len(ps)-k+1):
        if ps[i] == '-':
            moves += 1
            for j in range(i, i+k):
                flip = '+' if ps[j] == '-' else '-'
                ps[j] = flip
    if all(x == '+' for x in ps):
        return moves
    else:
        return 'IMPOSSIBLE'


with open(output_file, 'w') as dsout:
    for h in range(t):
        test = tests[h]

        if all(x == '+' for x in test[0]):
            dsout.write("Case #{}: {}\n".format(h+1, 0))
            print "TEST {} K={} => 0".format(test[0], test[1])
            continue
        else:
            minimum = minimumFlips(test[0], int(test[1]))
            print "TEST {} K={} => {}".format(test[0], test[1], minimum)
            dsout.write("Case #{}: {}\n".format(h+1, minimum))
