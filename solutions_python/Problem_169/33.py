import pulp
MAX = 1e13

def solve(ca):
    n, v, x = raw_input().split()
    n = int(n)
    v = float(v)
    x = float(x)

    info = [map(float, raw_input().split()) for i in range(n)]
    problem = pulp.LpProblem('pname', pulp.LpMinimize)
    xv = [pulp.LpVariable('var%d'%i, 0, MAX, 'Continuous') for i in range(n)]
    ans = pulp.LpVariable('ans', 0, MAX, 'Continuous')

    problem += ans

    problem += pulp.lpSum([info[i][0] * xv[i] for i in range(n)]) == v
    problem += pulp.lpSum([info[i][0] * info[i][1] * xv[i] for i in range(n)]) == v * x

    for i in range(n):
        problem += xv[i] <= ans
    
    
    #print problem
    status = problem.solve()
    if pulp.LpStatus[status] == 'Infeasible':
        print "Case #%d: IMPOSSIBLE"%ca
        return
    print "Case #%d: %.8f"%(ca, ans.value())
    
for i in range(int(raw_input())):
    solve(i + 1)
