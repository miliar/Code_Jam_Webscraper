__author__ = 'zumzoom'


if __name__ == '__main__':
    with open('input.txt') as inf:
        with open('output.txt', 'w') as of:
            t = int(inf.readline())
            for k in range(t):
                tokens = inf.readline().split()
                a, b = int(tokens[0]), tokens[1]
                s = 0
                ans = 0
                for i in range(a + 1):
                    if s < i:
                        ans += i - s
                        s += i - s
                    s += int(b[i])
                of.write("Case #{}: {}\n".format(k + 1, ans))
