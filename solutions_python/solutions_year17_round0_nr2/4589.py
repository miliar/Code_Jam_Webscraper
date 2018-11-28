def isTidy(n):
    p = 10
    while n:
        n, r = divmod(n, 10)
        if r > p:
            return False
        p = r
    return True

def solve(n):
    while n > 0:
        if isTidy(n):
            return n
        n -= 1

def problemB():
    T = int(input())
    for i in range(T):
        n = int(input())
        solution = solve(n)
        print('Case #{}: {}'.format(i+1, solution))

problemB()
