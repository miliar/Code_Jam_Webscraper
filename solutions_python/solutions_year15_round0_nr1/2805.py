def solve(i):
    n, s = fin.readline().split()
    n = int(n)
    s = list(map(int, list(s)))
    ans = 0
    stand = 0
    for j in range(n + 1):
        if stand < j:
            ans += j - stand
            stand = j
        stand += s[j]
    fout.write("Case #" + str(i + 1) + ": " + str(ans) + "\n")
    
    
fin = open("Alarge.in")
fout = open("Alarge.out", "w")
for i in range(int(fin.readline())):
    solve(i)
fin.close()
fout.close()