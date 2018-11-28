quart = [None] * 5
quart[1] = [None, 1, 2, 3, 4]
quart[2] = [None, 2, -1, 4, -3]
quart[3] = [None, 3, -4, -1, 2]
quart[4] = [None, 4, 3, -2, -1]

letterDict = {'1': 1, 'i': 2, 'j': 3, 'k': 4}


def quarternion(L, X, s):
    i, j, k = 0, len(s)-1, 0
    left, right, Z = 1, 1, 1

    while i < len(s):
        sign = -1 if left < 0 else 1
        left = sign * quart[abs(left)][letterDict[s[i]]]
        if left == 2:
            break
        i += 1

    while j >= 0:
        sign = -1 if right < 0 else 1
        right = sign * quart[letterDict[s[j]]][abs(right)]
        if right == 4:
            break
        j -= 1

    while k < L:
        sign = -1 if Z < 0 else 1
        Z = sign * quart[abs(Z)][letterDict[s[k]]]
        k += 1

    # print(i, j, Z)
    if i >= j:
        return False
    if X == 1 and Z == -1:
        return True
    if X > 1:
        if X % 4 == 1:
            return Z == -1
        if X % 4 == 2:
            return Z != 1
        if X % 4 == 3:
            return Z == -1



if __name__ == '__main__':
    TC = int(raw_input())

    for tc in range(1, TC+1):
        L, X = [int(i) for i in raw_input().split()]
        s = raw_input() * X
        result = quarternion(L, X, s)
        if result:
            print("Case #" + str(tc) + ": YES")
        else:
            print("Case #" + str(tc) + ": NO")

