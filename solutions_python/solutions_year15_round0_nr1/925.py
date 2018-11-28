def f(n, A):
    already = 0
    need = 0
    for i in range(n + 1):
        if i > already and A[i] > 0:
            need += i - already
            already = i
        already += A[i]
    return need


fin = open('A-large.in')
fout = open('A-large.out', 'w')
n = int(fin.readline())
for i in range(n):
    k, A = fin.readline().split()
    k = int(k)
    A = list(A)
    for j in range(len(A)):
        A[j] = int(A[j])
    if i == 2:
        pass
    fout.write("Case #" + str(i + 1) + ": " + str(f(k, A)) + "\n")
fin.close()
fout.close()