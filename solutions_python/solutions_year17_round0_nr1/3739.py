def reverse(s, k, i_):
    s_list = list(s)
    for l in range(i_, k + i_):
        if s[l] == "-":
            s_list[l] = "+"
        else:
            s_list[l] = "-"
    return "".join(s_list)


def check_end(check_):
    return_flg = True
    for i in range(len(check_)):
        if check_[i] == "-":
            return_flg = False
            break
    return return_flg


T = int(input())
for i in range(1, T + 1):
    inputs = input().split()
    S = inputs[0]
    K = int(inputs[1])
    count = 0
    for j in range(0, len(S) - K + 1):
        if S[j] == "-":
            S = reverse(S, K, j)
            count += 1

    check = S[-K:]
    if check_end(check):
        print("Case #" + str(i) + ": " + str(count))
    else:
        print("Case #" + str(i) + ": IMPOSSIBLE")
