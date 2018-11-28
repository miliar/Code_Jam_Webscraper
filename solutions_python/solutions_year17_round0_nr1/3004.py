import sys

sys.stdin = open("A-large.in")
f = open("p1.out", "w")

n = int(input())

for zzz in range(n):
    row, k = input().split()
    k = int(k) - 1
    count = 0
    row = list(row)
    for i in range(len(row) - 1, k - 1, -1):
        if row[i] == '-':
            count += 1
            for j in range(i - k, i + 1):
                if row[j] == '+':
                    row[j] = '-'
                else:
                    row[j] = '+'
    
    f.write("Case #" + str(zzz + 1) + ": ")

    if '-' in row:
        f.write("IMPOSSIBLE")
    else:
        f.write(str(count))
    f.write("\n")

f.close()
