import sys

def ones(length):
    num = 0

    for _ in range(length):
        num = num * 10
        num = num + 1

    return num

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())

    last_digit = N % 10
    number_len = len(str(N))

    answer = ones(number_len)
    additive = ones(number_len)

    if answer > N:
        answer = ones(number_len - 1)
        additive = ones(number_len - 1)

    while True:
        if additive == 0:
            break
        elif (additive + answer) <= N and answer % 10 != 9:
            answer = answer + additive
        else:
            additive = int(additive / 10)

    print("Case #" + str(_ + 1) + ": " + str(answer))
