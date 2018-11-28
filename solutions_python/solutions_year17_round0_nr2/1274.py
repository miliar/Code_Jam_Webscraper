'''
Tidy Numbers
'''


def main():
    t = int(input())
    for x in range(1, t + 1):
        N = input()
        y = N
        for i in range(len(N) - 1):
            if N[i] > N[i + 1]:
                while i > 0 and N[i] == N[i - 1]:
                    i -= 1
                y = N[:i] + str(int(N[i]) - 1) + '9' * (len(N) - i - 1)
                break

        print ("Case #{}: {}".format(x, y.lstrip('0')))


if __name__ == '__main__':
    main()
