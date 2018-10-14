def is_tidy(n):
    sn = str(n)
    sn = sn[::-1]
    for i in range(1, len(sn)):
        if sn[i] > sn[i - 1]:
            return False
    return True

f = open('out.txt', 'w')
t = int(input())
res = []
for i in range(t):
    n = int(input())
    for j in range(n, 0, -1):
        if is_tidy(j):
            res.append(j)
            break

for i in range(len(res)):
    print('Case #' + str(i + 1) + ':', res[i])
