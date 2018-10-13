
INPUT_FILE = "./B-large.in"
OUTPUT_FILE = "./B-large.out"


if __name__ == '__main__':
    with open(INPUT_FILE, "r") as fin, open(OUTPUT_FILE, "w") as fout:
        T = int(fin.readline())
        for case_i in range(1, T + 1):
            n = list(map(int, reversed(list(fin.readline()[:-1]))))
            ans = []
            for i, digit in enumerate(n):
                if i >= 1 and digit > ans[i - 1]:
                    for j in range(i):
                        ans[j] = 9
                    ans.append(digit - 1)
                else:
                    ans.append(digit)
            
            ans = sum([digit * (10**i) for i, digit in enumerate(ans)])
            print('Case #{}: {}'.format(case_i, ans), file = fout)
