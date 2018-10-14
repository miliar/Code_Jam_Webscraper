def tidy(num):
    num = list(num)
    for i in range(len(num) - 1, 0, -1):
        if int(num[i]) < int(num[i - 1]):
            for j in range(i, len(num)):
                num[j] = '9'
            num[i] = '9'
            num[i - 1] = str(int(num[i - 1]) - 1)
    return str(int(''.join(num)))


def main():
    nb_test = int(input())
    for _ in range(nb_test):
        arg = input()
        print('Case #' + str(_ + 1) + ': ' + tidy(arg))

if __name__ == '__main__':
    main()