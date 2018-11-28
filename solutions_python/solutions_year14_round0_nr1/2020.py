def solve(a1, a2, b1, b2):
    x = set(b1[a1-1]) & set(b2[a2-1])
    if len(x) == 1:
        return list(x)[0]
    elif len(x) < 1:
        return 'Volunteer cheated!'
    elif len(x) > 1:
        return 'Bad magician!'

def main():
    n = int(input())
    for i in range(n):
        a1 = int(input())
        b1 = [list(map(int, input().split())) for j in range(4)]
        a2 = int(input())
        b2 = [list(map(int, input().split())) for j in range(4)]
        ans = solve(a1, a2, b1, b2)
        print("Case #{}: {}".format(i+1, ans))

main()
