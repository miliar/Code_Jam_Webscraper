inFile = open('b.in', 'r')
outFile = open('b.out', 'w')

n = int(inFile.readline())
for i in range(n):
    a = map(int, inFile.readline().split())
    ans = 0
    for j in range(3, len(a)):
        if a[j] >= a[2] and 3*a[2]-2 <= a[j]:
            ans += 1
        elif a[1] > 0 and a[j] >= a[2] and 3*a[2]-4 <= a[j]:
            a[1] -= 1
            ans += 1
    outFile.write('Case #{0}: {1}\n'.format(i+1, ans))

inFile.close()
outFile.close()
