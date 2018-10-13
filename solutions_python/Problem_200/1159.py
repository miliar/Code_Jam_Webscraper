import sys

def tidy(n):
    isDone = False
    while not isDone:
        isLoop = True

        for i in range(0, len(n) - 1):
            if n[i] > n[i + 1]:
                n = n[:i] + str(int(n[i]) - 1) + '9' * (len(n) - i - 1)
                isLoop = False
                break
        isDone = isLoop
    return int(n)

if __name__ == '__main__':
    test = open(sys.argv[1], 'r')
    for i in range(int(test.readline().strip())):
        print('Case #' + str(i + 1) + ': ' + str(tidy(test.readline().strip())))
