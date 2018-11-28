fin = open('input.txt')
fout = open('output.txt', 'w')

T = int(fin.readline())

for t in range(1, T + 1):
    temp = fin.readline().split()
    A, B, K = int(temp[0]), int(temp[1]), int(temp[2])
    s = 0
    for i in range(A):
        for j in range(B):
            if (i & j) < K:
                s += 1
    fout.write("Case #" + str(t) + ": " + str(s) + "\n")
fin.close()
fout.close()