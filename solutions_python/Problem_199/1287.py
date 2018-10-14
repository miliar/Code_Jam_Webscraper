def solve():
    s, k = input().split()
    k = int(k)

    s = list(s)
    answer = 0

    for i in range(len(s) - k + 1):
        if s[i] == '-':
            answer += 1
            for j in range(k):
                s[i + j] = '+' if s[i + j] == '-' else '-'

    if all(map(lambda x: x == '+', s)):
        return answer
    return 'IMPOSSIBLE'

t = int(input())
for i in range(1, t + 1):
    print('Case #{}: {}'.format(i, solve()))
