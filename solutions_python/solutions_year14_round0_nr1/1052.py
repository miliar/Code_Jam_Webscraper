# This code was interpreted using CPython 3.3.4
# python3 Main.py <


def read():
    row = int(input())
    mat = []
    for _ in range(4):
        mat.append([int(card) for card in input().split(' ')])

    return mat[row -1]

T = int(input())
for T_ in range(T):
    l1 = read()
    l2 = read()

    diff = list(set(l1).intersection(set(l2)))
    diff_len = len(diff)

    ans = ""
    if diff_len == 0:
        ans = "Volunteer cheated!"
    elif diff_len == 1:
        ans = str(diff[0])
    else:
        ans = "Bad magician!"

    print("Case #{0}: {1}".format(T_+1, ans))

