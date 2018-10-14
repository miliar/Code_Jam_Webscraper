def solve(x):
    for i in range(1, len(x)):
        if (x[i - 1] > x[i]):
            x[i - 1] -= 1
            for j in range(i, len(x)):
                x[j] = 9
            j = i - 1
            while (x[j] == -1):
                x[j - 1] -= 1                
                x[j] = 9
                j -= 1
            return solve(x)
    return x
    

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())
for case in range(1, t + 1):
    ans = solve(list(map(int, fin.readline().strip())))
    i = 0
    while ((i < len(ans) - 1) and (ans[i] == 0)):
        i += 1
    fout.write("Case #" + str(case) + ": " + ''.join(map(str, ans[i:])) + "\n")

fin.close()
fout.close()