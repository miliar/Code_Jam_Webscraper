def flip(pancakes, start, k):
    for i in range(start, start + k):
        pancakes[i] = '+' if pancakes[i] == '-' else '-'

def flips(pancakes, k):
    c = 0
    for start in range(len(pancakes) - k + 1):
        if pancakes[start] == '-':
            flip(pancakes, start, k)
            c += 1

    if set(pancakes) != set(['+']):
        return 'IMPOSSIBLE'

    return str(c)

def main():
    N = int(input())
    for t in range(1, N + 1):
        pancakes, k = input().strip().split()
        pancakes = list(pancakes)
        k = int(k)
        print("Case #%d: %s" % (t, flips(pancakes, k)))

main()
