import math

tc = int(input())

def getAnswer(number):
    if (number % 2 == 0):
        return (int(number/2), int(number/2) - 1)
    else:
        return (int(number/2), int(number/2))

for etc in range(tc):
    N, K = map(int, input().strip().split())

    # Logic
    diff = N - K + 1

    # higherDegreeOfK
    k = 2
    while (k <= K):
        k = k*2

    group = int(k/2)

    # print (group)

    answer = (getAnswer(math.ceil(diff / group)))

    print ("Case #" + str(etc + 1) + ": " + str(answer[0]) + " " + str(answer[1]))
