def solve(pancakes):
    # solver for small dataset
    pancakes.sort(reverse = True)
    for _ in range(3):
        pancakes.append(0)
    patterns = []
    pattern_111 = pancakes[0]
    pattern_211 = max((pancakes[0] + 1) / 2, pancakes[1]) + 1
    pattern_311 = max((pancakes[0] + 2) / 3, pancakes[1]) + 2
    pattern_221 = max((pancakes[0] + 1) / 2, (pancakes[1] + 1) / 2, pancakes[2]) + 2
    pattern_321 = max((pancakes[0] + 2) / 3, (pancakes[1] + 1) / 2, pancakes[2]) + 3
    pattern_222 = max((pancakes[0] + 1) / 2, (pancakes[1] + 1) / 2, pancakes[3]) + 3
    minimum_minite = min(pattern_111, pattern_211, pattern_311,
                         pattern_321, pattern_221, pattern_222)
    #print pancakes[:-3], minimum_minite
    return minimum_minite

def answer(outputs):
    for i, output in enumerate(outputs):
        print 'Case #{0}: {1}'.format(i+1, output)
    
def main():
    num_samples = input()
    outputs = []
    for _ in range(num_samples):
        num_diner = input()
        pancakes = map(int, raw_input().rstrip().split())
        minimum_minite = solve(pancakes)
        outputs.append(minimum_minite)
    answer(outputs)

main()
