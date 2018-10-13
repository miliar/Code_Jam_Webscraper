import random

def load_tests():
    tests = []
    with open('pancake_flip.txt') as data:
        for line in data.readlines()[1:]:
            pancakes, gap = line.split(" ")
            gap = int(gap)
            tests.append([pancakes, gap])
    return tests

def run_test(pancakes, gap):
    runs = 0
    while pancakes != ('+'*len(pancakes)):
        pancakes = flip(pancakes, random.randint(0, len(pancakes)-gap), gap)
        runs += 1
        if runs > 10000:
            raise Exception()
    return runs

def flip(pancakes, start, gap):
    list_pancakes = list(pancakes)
    for i, char in enumerate(pancakes[start:start+gap]):
        list_pancakes[i+start] = '+' if char == '-' else '-'
    return ''.join(list_pancakes)

def main():
    tests = load_tests()
    for j, test in enumerate(tests):
        best = 1000000
        for i in range(10000):
            try:
                result = run_test(*test)
                if result < best:
                    best = result
            except Exception:
                best = "IMPOSSIBLE"
                break
        print("Case #{}: {}".format(j+1, best))

main()
