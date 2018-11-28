def flip(pancakes, i, k):
    for j in range(i, i + k):
        pancakes[j] = '+' if pancakes[j] == '-' else '-'

def test_case():
    pancakes, K = input().split()
    K = int(K)
    pancakes = [ p for p in pancakes ]
    flips = 0
    for i in range(len(pancakes) - K + 1):
        if pancakes[i] == '-':
            flip(pancakes, i, K)
            flips += 1
    if '-' in pancakes:
        return 'IMPOSSIBLE'
    else:
        return flips

def main():
    T = int(input())
    for t in range(T):
        print('Case #{}:'.format(t + 1), test_case())

if __name__ == '__main__':
    main()
