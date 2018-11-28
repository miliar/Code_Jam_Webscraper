
def solve(N):
    if len(N) == 1:
        return N
    isOrderd = True
    for i in range(0, len(N) - 1):
        if N[i] > N[i + 1]:
            isOrderd = False
            break
    if isOrderd:
        return N
    if len(N) == 2:
        n = str(int(N[0]) - 1) + "9"

    tmp = "".rjust(len(N), "9")
    tmp = N[0] + tmp[1:]
    if int(tmp) <= int(N):
        return tmp
    for i in range(1, 10):
        x = int(tmp[1]) - 1
        if x < int(N[0]):
            if int(N[0]) > 1:
                return str(int(N[0]) - 1) + "".rjust(len(N) - 1, "9")
            else:
                return "".rjust(len(N) - 1, "9")
        tmp = tmp[:1] + str(x) + tmp[2:]
        if int(tmp) <= int(N):
            return tmp


t = int(input())
for i in range(1, t + 1):
    N = input()
    retval = solve(N)
    print("Case #{}: {}".format(i, retval))
