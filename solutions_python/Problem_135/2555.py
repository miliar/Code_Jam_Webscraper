T = int(input())

for t in range(T):
    row1 = int(input()) - 1
    for r in range(4):
        if r == row1:
            set1 = set(map(int, input().split()))
            continue
        input()

    row2 = int(input()) - 1
    for r in range(4):
        if r == row2:
            set2 = set(map(int, input().split()))
            continue
        input()

    ans = set1.intersection(set2)

    print('Case #{}: '.format(t+1), end='')
    if len(ans) == 0:
        print('Volunteer cheated!')
    elif len(ans) == 1:
        print(ans.pop())
    else:
        print('Bad magician!')
