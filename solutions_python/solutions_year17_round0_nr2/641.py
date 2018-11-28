test_cnt = int(input())

def tidy(num):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False
    return True

for test in range(1, test_cnt + 1):
    num = list(input())
    num = [int(digit) for digit in num]
    candidates = [num]
    for i in range(len(num)):
        if num[i] != 0:
            candidates.append(num[:i] + [num[i] - 1] + ([9] * (len(num) - i - 1)))
    candidates = [n for n in candidates if tidy(n)]
    best = max(candidates)
    best = int(''.join([str(digit) for digit in best]))
    print("Case #" + str(test) + ": " + str(best))
