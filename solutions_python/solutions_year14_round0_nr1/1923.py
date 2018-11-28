def solve(num):
    a = int(input())
    A = [input().split() for i in range(4)]
    b = int(input())
    B = [input().split() for i in range(4)]
    Ans = set(A[a - 1]) & set(B[b - 1])
    print("Case #" + str(num) + ": ", end = "")
    if len(Ans) == 1:
        print(Ans.pop())
    elif len(Ans) == 0:
        print("Volunteer cheated!")
    else:
        print("Bad magician!")

T = int(input())
for i in range(T):
    solve(i + 1)


