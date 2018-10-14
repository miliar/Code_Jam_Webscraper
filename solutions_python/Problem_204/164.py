def round_divide(n, d):
    return (n + d / 2) / d

T = int(raw_input())

for i in xrange(T):
    [N, P] = map(int, raw_input().split())
    true_ingredients = map(int, raw_input().split())

    available = []

    for j in xrange(N):
        row = map(int, raw_input().split())
        result = []
        for item in row:
            item_spec = []
            qual = round_divide(item, true_ingredients[j])
            #print abs(qual * true_ingredients[j] - item)
            #print true_ingredients[j] * qual * 0.1

            qual_0 = qual
            while true_ingredients[j] * qual - 10 * abs(qual * true_ingredients[j] - item) >= 0:
                item_spec.append(qual)
                qual += 1

            qual = qual_0 - 1
            while qual > 0 and true_ingredients[j] * qual - 10 * abs(qual * true_ingredients[j] - item) >= 0:
                item_spec.append(qual)
                qual -= 1

            result.append(item_spec)

        available.append(result)

    #print available

    output = 0

    if N == 1:
        for item in available[0]:
            if len(item) > 0:
                output += 1

    else: # small test case 1 or 2
        #available[0].sort(lambda x, y: cmp(len(x), len(y)))
        #available[1].sort(lambda x, y: cmp(len(x), len(y)))
        for item in available[0]:
            found = False
            for spec in item:
                for j in xrange(len(available[1])):
                    #print available
                    if available[1][j].count(-1) == 0 and available[1][j].count(spec) != 0:
                        available[1][j].append(-1)
                        found = True
                        output += 1
                        break

                if found:
                    break

    print "Case #%d: %d" % (i + 1, output)
