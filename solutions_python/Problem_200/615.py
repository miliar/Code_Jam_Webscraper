def solve(number):
    if len(number) < 2:
        return number

    nl = list(number)
    i = 0
    while nl[i] <= nl[i+1]:
        i += 1
        if i == len(nl) - 1:
            return number

    if nl[i] == '1':
        return (len(nl) - 1) * '9'

    prev = nl[i]
    while nl[i] == prev:
        i -= 1
        if i == -1:
            break
    nl[i+1] = chr(ord(prev) - 1)
    i += 2
    return ''.join(nl[:i]) + ((len(nl) - i) * '9')

T = int(input())

solutions = [solve(input()) for _ in range(T)]
for i, s in enumerate(solutions):
    print("Case #{}: {}".format(i+1, s))
