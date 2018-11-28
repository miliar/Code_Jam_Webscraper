input = open('A-large.in', 'r')
output = open('A-large.out', 'w')
N = int(input.readline())
for case in range(1, N + 1):
    print("Case #", case, sep = "", end = ": ", file = output)
    data = input.readline().rstrip().split()
    state, k = data[0], int(data[1])
    state = [1 if x=="+" else 0 for x in list(state)]
    ans = 0
    for i in range(len(state) - k + 1):
        if not state[i]:
            ans += 1
            for j in range(i, i+k):
                state[j] = 1 - state[j]
    if 0 in state[-k:]:
        print("IMPOSSIBLE", file = output)
    else:
        print(ans, file = output)
input.close()
output.close()