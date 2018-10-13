import random


def is_tidy(number):
    n = str(number)
    p = ''.join(sorted(n))
    return p == n


def brute(number):
    n = int(number)
    while n:
        if is_tidy(n):
            return str(n)
        n -= 1


def optimal(number):
    n = str(number)
    if is_tidy(n):
        return n
    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            lb = i
            break
    fb = None
    for i in range(lb - 1, 0, -1):
        if (int(n[i]) - 1) >= int(n[i - 1]):
            fb = i
            break
    if fb:
        result = ['0' for i in range(len(n))]
        for i in range(len(n)):
            if i < fb:
                result[i] = n[i]
            elif i == fb:
                result[i] = str(int(n[i]) - 1)
            else:
                result[i] = '9'
        return ''.join(result)
    else:
        result = ''
        if n[0] != '1':
            result = str(int(n[0]) - 1)
        return result + '9' * (len(n) - 1)


def test():
    NUM_ROUNDS = 10 ** 4
    MAX_NUM = 10 ** 5
    for i in range(NUM_ROUNDS):
        print(i)
        tar = random.randint(1, MAX_NUM)
        opt = optimal(tar)
        bru = brute(tar)
        if opt != bru:
            print(tar, opt, bru)
            break


T = int(input())
for I in range(1, T+1):
    inp = int(input())
    print("Case #{}: {}".format(I, optimal(inp)))
