from sys import stdin

stdin = open("A-large.in.txt")
T = int(stdin.readline())
with open('Aout.txt', 'w', encoding="utf-8") as p:
    for i, line in enumerate(stdin, start=1):
        p.write(f'Case #{i}: ')
        n = line.strip().split()

        S = [x == '+' for x in n[0]]
        K = int(n[1])

        count = 0
        while not all(S):
            ind = S.index(False)
            if len(S) - ind < K:
                p.write("IMPOSSIBLE\n")
                break
            for i in range(ind, ind + K):
                S[i] = not S[i]

            count += 1
        else:
            p.write(str(count) + "\n")
