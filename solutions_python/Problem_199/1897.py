T = int(input())

def solution():
    s, k = input().split()
    k = int(k)
    s = list(s)
    answer = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            for j in range(i, i + k):
                s[j] = '-' if s[j] == '+' else '+'
            answer += 1
    if '-' in s:
        return "IMPOSSIBLE"
    return answer

for test in range(1, T + 1):
    print("Case #{}: {}".format(test, solution()))