T = int(input())

def solution():
    def is_beatiful(n):
        s = list(str(n))
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                return False
        return True

    n = int(input())
    if is_beatiful(n):
        return n
    s = list(str(n))
    answer = 0
    for i in range(len(s) - 1):
        if s[i] == '0':
            continue
        a = int(''.join(s[:i] + [str(int(s[i]) - 1)] + ['9'] * (len(s) - i - 1)))
        if is_beatiful(a):
            answer = max(answer, a)
    assert answer <= n
    return answer





for test in range(1, T + 1):
    print("Case #{}: {}".format(test, solution()))