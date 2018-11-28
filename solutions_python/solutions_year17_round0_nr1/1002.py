input_name = 'A-large.in'
output_name = 'large-output'

input = open(input_name, 'r')
output = open(output_name, 'w')


line_nb = 0
for line in input:
    line_nb += 1
    if line_nb == 1:
        T = int(line)
        arr = []
        arrK = []
    else:
        cookies, K = line.split(' ')
        K = int(K)
        arr.append(cookies)
        arrK.append(K)

input.close()


def tonumber(cookies):
    arr = []
    for i in range(len(cookies)):
        if cookies[i] == '+':
            arr.append(1)
        else:
            arr.append(0)
    return arr


def flip(arr, i, K):
    for j in range(i, i + K):
        arr[j] = 1 - arr[j]
    return arr


def good(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            return False
    return True


def solve(cookies, K):
    arr = tonumber(cookies)
    nb = 0
    for i in range(len(arr) - K + 1):
        if arr[i] == 0:
            arr = flip(arr, i, K)
            nb += 1
    if good(arr):
        return nb
    else:
        return "IMPOSSIBLE"

print T
print arrK
print arr

for i in range(T):
    sol = solve(arr[i], arrK[i])
    output.write("Case #" + str(i + 1) + ": " + str(sol) + "\n")

output.close()
