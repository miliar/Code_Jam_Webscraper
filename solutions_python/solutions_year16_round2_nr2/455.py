def gen(A, a, b, s1, s2, i, j):
    if i < len(a):
        if a[i] == "?":
            for dig1 in range(10):
                gen(A, a, b, s1 + str(dig1), s2, i + 1, j)
        else:
            gen(A, a, b, s1 + str(a[i]), s2, i + 1, j)
    elif j < len(b):
        if b[j] == "?":
            for dig1 in range(10):
                gen(A, a, b, s1, s2 + str(dig1), i, j + 1)
        else:
            gen(A, a, b, s1, s2 + str(b[j]), i, j + 1)
    else:
        A.append([s1, s2])


def tcase():
    a, b = input().split()
    length = len(a)
    A = []
    gen(A, a, b, "", "", 0, 0)
    B = []
    mn = float("inf")
    for l in A:
        if abs(int(l[0]) - int(l[1])) < mn:
            mn = abs(int(l[0]) - int(l[1]))
    for l in A:
        if abs(int(l[0]) - int(l[1])) == mn:
            B.append(l)
    C = []
    mn = float("inf")
    for l in B:
        if int(l[0]) < mn:
            mn = int(l[0])
    for l in B:
        if int(l[0]) == mn:
            C.append(l)
    D = []
    mn = float("inf")
    for l in C:
        if int(l[1]) < mn:
            mn = int(l[1])
    for l in C:
        if int(l[1]) == mn:
            D.append(l)
    return D[0]



t = int(input())
for i in range(t):
    print("Case #" + str(i + 1) + ": " + " ".join(tcase()))