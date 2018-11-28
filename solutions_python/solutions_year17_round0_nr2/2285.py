def solve(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            n[i] -= 1
            for j in range(i+1, len(n)):
                n[j] = 9
            for j in range(i):
                if n[i-j-1] <= n[i-j]:
                    break
                else:
                    n[i-j] = 9
                    n[i-j-1] -= 1
            break
    return str(int("".join(map(str,n))))

fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

t = int(fin.readline())

for i in range(t):
    n = map(int, list(fin.readline())[:-1])
    fout.write("Case #" + str(i+1) + ": " + solve(n) + "\n")
