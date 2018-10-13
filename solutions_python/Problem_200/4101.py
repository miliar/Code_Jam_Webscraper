T = int(input())

def solve_simple(N):
    while N > 0:
        nstr = str(N)
        if nstr == ''.join(sorted(nstr)):
            return N
        N -= 1

def solve_large(N):
    nstr = str(N)
    if nstr == ''.join(sorted(nstr)):
        return N

    high = nstr[0]
    ind = 0
    for i, c in enumerate(nstr[1:], 1):
        if c < high:
            break
        elif c > high:
            high = c
            ind = i
    news = nstr[:ind] + str(int(nstr[ind]) - 1) + '9'*(len(nstr) - ind - 1)
    return int(news)
            

for _ in range(1, T+1):
    n = int(input())
    print("Case #{}: {}".format(_, solve_large(n)))
