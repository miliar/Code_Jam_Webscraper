def digits():
    n = list(map(int, list(str(input()).rstrip())))
    for _ in range(20):
        for i in range(1, len(n)):
            if n[i - 1] > n[i]:
                n[i - 1] -= 1
                for j in range(i, len(n)):
                    n[j] = 9
    return n

def solve():
    x = digits()
    t = 0
    for e in x:
        t = 10 * t + e
    return t

if __name__ == '__main__':
    t = int(str(input()).rstrip())
    for i in range(1, t + 1):
        print('Case #' + str(i) + ': ' + str(solve()))
