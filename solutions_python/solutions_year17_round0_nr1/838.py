def flip(pancakes, i, K, n_flips):
    for j in range(i, i+K):
        pancakes[j] = not pancakes[j]
    return (pancakes, n_flips + 1)

def case(n, pancakes, K):
    n_flips = 0
    print("case #{}: {} {}".format(n, pancakes, K))
    def print_(s): 
        print " ", s
    N = len(pancakes)
    for i in range(0, N - K + 1):
        print_("pancakes {} -> {}: {}".format(i, i+K, pancakes[i:i+K]))
        if not pancakes[i]:
            print_("flipping")
            pancakes, n_flips = flip(pancakes, i, K, n_flips)
        print_("pancakes: {}".format(pancakes))
    return pancakes, n_flips

import fileinput

stdin = fileinput.input()

T = int(next(stdin))
print "T:", T

for n in range(1, T+1):
    case_input = next(stdin)
    pancakes, K = case_input.split(' ')
    K = int(K)
    pancakes = [ c == '+' for c in pancakes ]
    pancakes, n_flips = case(n, pancakes, K)
    result = str(n_flips) if all(pancakes) else "IMPOSSIBLE"
    print "Case #{}: {}".format(n, result)

        
