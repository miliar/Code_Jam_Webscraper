import sys

def pancakes(pancakes, k):
    pancakes = map(lambda x: 0 if x == '+' else 1, pancakes)
    flips = []
    # print str(pancakes)
    for i in range(len(pancakes) - k + 1):
        num_flips = 0
        for j in range(max(0, i - k + 1), i):
            num_flips ^= flips[j]
        flips.append(pancakes[i] ^ num_flips)

    for i in range(len(pancakes) - k + 1, len(pancakes)):
        num_flips = 0
        for j in range(max(0, i - k + 1), min(i, len(pancakes) - k + 1)):
            num_flips ^= flips[j]
        if pancakes[i] ^ num_flips == 1:
            return "IMPOSSIBLE"

    return sum(flips)

if __name__ == '__main__':
    test = open(sys.argv[1], 'r')
    for i in range(int(test.readline().strip())):
        pcks, k = test.readline().split(' ')
        print('Case #' + str(i + 1) + ': ' + str(pancakes(pcks, int(k))))
