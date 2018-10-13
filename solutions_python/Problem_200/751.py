def decrement(sol, pos):
    if pos < 0:
        return sol
    if sol[pos] != 0:
        sol[pos] = sol[pos] - 1
        if pos != 0 and sol[pos-1] > sol[pos]:
            sol[pos] = 9
            return decrement(sol, pos-1)
        else:
            return sol
    else:
        sol[pos] = 9
        return decrement(sol, pos - 1)
def solve():
    N = raw_input()
    N = map(int, list(N))
    if len(N) == 1:
        return N[0]
    sol =[0] * len(N)
    prev = 0
    dropped = False
    for i in range(len(N)):
        if dropped:
            sol[i] = 9
        elif N[i] >= prev:
            sol[i] = N[i] 
            prev = sol[i]
        else:
            # drop
            # update previous
            dropped = True
            sol = decrement(sol, i-1)
            sol[i] = 9
    sol = int(''.join(map(str, sol)))
    sol = max(int('9'*(len(N) - 1)), sol)
    return sol

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(1, T+1):
        print "Case #{}: {}".format(i, solve())
