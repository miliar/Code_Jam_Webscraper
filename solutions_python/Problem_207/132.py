import math

fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

t = int(fin.readline())
for i in xrange(1, t + 1):
    N, R, O, Y, G, B, V = [int(s) for s in fin.readline().strip().split(" ")]

    if R == G and N == R + G:
        ans = 'RG' * R
        print>> fout, "Case #{}: {}".format(i, ans)
        continue
    if Y == V and N == Y + V:
        ans = 'YV' * Y
        print>> fout, "Case #{}: {}".format(i, ans)
        continue
    if B == O and N == B + O:
        ans = 'BO' * B
        print>> fout, "Case #{}: {}".format(i, ans)
        continue

    if (R <= G and G != 0) or (Y <= V and V != 0) or (B <= O and O != 0):
        print>> fout, "Case #{}: IMPOSSIBLE".format(i)
        continue

    c1 = 'R'
    c2 = 'Y'
    c3 = 'B'
    n1 = R - G
    n2 = Y - V
    n3 = B - O
    if n1 < n2:
        t = n1
        n1 = n2
        n2 = t
        t = c1
        c1 = c2
        c2 = t
    if n1 < n3:
        t = n1
        n1 = n3
        n3 = t
        t = c1
        c1 = c3
        c3 = t

    if n1 > n2 + n3:
        print>> fout, "Case #{}: IMPOSSIBLE".format(i)
        continue

    remain = n2 + n3 - n1
    ans = ''
    for j in range(remain):
        ans = ans + c2 + c3 + c1
    for j in range(n2 - remain):
        ans += c2 + c1
    for j in range(n3 - remain):
        ans += c3 + c1

    SO = 'B' + 'OB' * O
    SG = 'R' + 'GR' * G
    SV = 'Y' + 'VY' * V

    ans = ans.replace('B', 'O', 1).replace('R', 'G', 1).replace('Y', 'V', 1)
    ans = ans.replace('O', SO, 1).replace('G', SG, 1).replace('V', SV, 1)
    print>>fout, "Case #{}: {}".format(i, ans)

fin.close()
fout.close()
