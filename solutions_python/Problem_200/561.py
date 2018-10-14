def solve(N):
    if not N:
        return ''
    lb = '9' * len(N)
    while int(lb) > int(N) and lb[0] > '1':
        lb = chr(ord(lb[0]) - 1) * len(N)
    if int(lb) > int(N):
        return solve('9' * (len(N) - 1))
    if lb[0] < N[0]:
        return lb[0] + '9' * (len(N) - 1)
    return lb[0] + solve(N[1:])

for t in range(1, int(input())+1):
    N = input()
    print("Case #{}: {}".format(t, solve(N)))
