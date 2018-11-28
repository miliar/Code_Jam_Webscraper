fi = open("B-large.in")
fo = open("B-large.out", "w")
t = int(fi.readline())
for i in range(t):
    n = list(map(int,fi.readline().strip()))
    for p in range(100):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                n[j] -= 1
                for k in range(j+1, len(n)):
                    n[k] = 9
    if n[0] == 0:
        del n[0]
    fo.write("Case #{}: {}\n".format(i+1, ''.join(map(str,n))))
