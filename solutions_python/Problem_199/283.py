
INPUT_FILE = "./A-large.in"
OUTPUT_FILE = "./A-large.out"


if __name__ == '__main__':
    with open(INPUT_FILE, "r") as fin, open(OUTPUT_FILE, "w") as fout:
        T = int(fin.readline())
        for case_i in range(1, T + 1):
            pancakes, k = fin.readline().split()
            pancakes = list(pancakes)
            k = int(k)
            s = len(pancakes)
            ans = 0
            for i in range(s - k + 1):
                if pancakes[i] == '-':
                    ans += 1
                    for j in range(i, i + k):
                        pancakes[j] = '+' if pancakes[j] == '-' else '-'

            ans = ans if pancakes.count('-') == 0 else 'IMPOSSIBLE'
            print('Case #{}: {} {}'.format(case_i, ans, ''.join(pancakes)))
            print('Case #{}: {}'.format(case_i, ans), file = fout)
