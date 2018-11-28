def solve(n):
    for i in range(1, len(n)):
        if sorted(n) == n:
            break
        n[len(n)-i] = '0'
        n = list(str(int(''.join(n)) - 10**(i-1)))
    return int(''.join(n))

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, solve(list(input()))))
