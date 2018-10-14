
def solve():
    N, M = map(int, input().split())
    b = []
    for _ in range(N):
        b.append(list(map(int, input().split())))

    alc = 0
    while b:
        m = min(map(min, b))
        ol = len(b)
        b = [row for row in b if max(row) > m]
        if ol == len(b):
            alc += 1
        else:
            alc = 0

        if alc > 1:
            return "NO"
          
        b = list(zip(*b))

    return "YES"

T = int(input())
for tn in range(T):
    print("Case #{0}: {1}".format(tn + 1, solve()))
