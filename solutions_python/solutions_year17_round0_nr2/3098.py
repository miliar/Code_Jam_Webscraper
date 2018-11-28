def test(t_num):
    n = input()
    while True:
        p = -1
        for i in range(len(n) - 1, 0, -1):
            if n[i - 1] > n[i] or n[i] == '0':
                p = i
                break
        if p == -1:
            break
        n = str(int(n) - int(n[p:]) - 1)
    print('Case #{}: {}'.format(t_num, n))

def test_dumb(t_num):
    def ok(s):
        for i in range(len(s) - 1, 0, -1):
            if int(n[i - 1]) > int(n[i]):
                return False
        return True
    n = input()
    while not ok(n):
        n = str(int(n) - 1)
    print('Case #{}: {}'.format(t_num, n))

t = int(input())

for i in range(1, t + 1):
    test(i)
