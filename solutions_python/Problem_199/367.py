def solution(line):
    s, k = line.split()
    k = int(k)
    s = [1 if x == '+' else 0 for x in s]
    flip_cnt = 0
    for i, _ in enumerate(s[:-k + 1]):
        if s[i] == 0:
            s[i : i + k] = [v^1 for v in s[i : i + k]]
            flip_cnt += 1
    if all(v == 1 for v in s):
        return str(flip_cnt)
    else:
        return 'IMPOSSIBLE'


n_tests = int(input())
for i in range(1, n_tests + 1):
    n = input()
    print('Case #{}: {}'.format(i, solution(n)))