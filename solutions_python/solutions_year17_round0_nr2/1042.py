import math

input_name = 'B-large.in'
output_name = 'large-output'

input = open(input_name, 'r')
output = open(output_name, 'w')


def fill9(arr, begin, l):
    for i in range(begin, l):
        arr[i] = 9
    return arr


def tonumber(arr):
    rep = 0
    for i in range(len(arr)):
        rep *= 10
        rep += arr[i]
    return rep


def solve(N):
    l = int(math.floor(math.log10(N)) + 1)
    arr = [0] * l
    n = N
    for i in range(l - 1, -1, -1):
        arr[i] = n % 10
        n = n / 10
    i = 0
    while i != l - 1:
        if arr[i] > arr[i + 1]:
            arr[i] = arr[i] - 1
            fill9(arr, i + 1, l)
            i = max(i - 1, 0)
        else:
            i = i + 1
    return tonumber(arr)


case = 0
for line in input:
    case += 1
    if case == 1:
        T = int(line)
    else:
        N = int(line)
        sol = solve(N)
        output.write("Case #" + str(case - 1) + ": " + str(sol) + "\n")

input.close()
output.close()
