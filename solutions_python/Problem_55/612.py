def OnceTime(k, g, people, N, n):
    n = n + 1
    if n > N:
        return people
    first = g[0]
    if (people == 0) or ((people + first) <= k):
        people = people + first
        g.remove(first)
        g.append(first)
        return OnceTime(k, g, people, N, n)
    return people
    
def RollerCoaster(R, k, N, g):
    if N == 1:
        return g[0] * R
    money = 0
    for i in range(0, R):
        money = money + OnceTime(k, g, 0, N, 0)
    return money

T = input()
for i in range(0, T):
    R, k, N = raw_input().split()
    R = int(R)
    k = int(k)
    N = int(N)
    g = raw_input().split()
    for j in range(0, len(g)):
        g[j] = int(g[j])
    print "Case #%s: %s" % (i + 1, RollerCoaster(R, k, N, g))
