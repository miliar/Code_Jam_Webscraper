'''
 Cruise Control
'''


def main():
    t = int(input())
    for x in range(1, t + 1):
        y = ''
        D, N = [int(i) for i in input().split()]
        max_time = 0
        for i in range(N):
            k, s = [int(j) for j in input().split()]
            r = (D - k) / s
            if r > max_time:
                max_time = r
        y = D / max_time

        print ("Case #{}: {:f}".format(x, y))


if __name__ == '__main__':
    main()
