def solve(solution):
    for d in range(len(solution) - 1):
        if solution[d + 1] < solution[d]:
            solution[d] -= 1
            solution = solution[:d + 1] + [9] * (len(solution) - d - 1)
            return False, solution
    return True, solution


t = int(input())
for i in range(t):
    n = input()
    sol = []
    for d in n:
        sol.append(int(d))
    finished, sol = solve(sol)
    while not finished:
        finished, sol = solve(sol)
        # print(sol)

    ans = ''.join(map(str, sol))
    if ans.startswith('0'):
        ans = (ans[1:])
    else:
        ans = (ans)
    print('Case #{0}: {1}'.format(i+1, ans))
