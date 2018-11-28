def last_tidy_number(N):
    digits = [int(x) for x in str(N)]
    for i in reversed(range(len(N)-1)):
        if digits[i] > digits[i+1]:
            digits[i] -= 1
            digits[i+1] = 9

    nine = False
    for i in range(len(N)):
        if nine:
            digits[i] = 9
        elif digits[i] == 9:
            nine = True

    return int(''.join([str(x) for x in digits]))

def result():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N = input()
        y = last_tidy_number(N)
        print("Case #{}: {}".format(i, y))

if __name__ == '__main__':
    result()