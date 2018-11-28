t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    e = -1
    p = []
    s = 0
    P = 0
    n = list(input())
    for j in range(len(n)):
        if s == 1:
            p.append(9) #+= 10 ** (len(n) - j - 1) * 9
        elif j == len(n) - 1:
            p .append(int(n[j]))
        elif int(n[j]) > int(n[j + 1]):
            p.append(int(n[j]) - 1)
            s = 1
            if e != -1:
                p[e] -= 1
                for k in range(e + 1, j + 1):
                    p[k] = 9 
        elif int(n[j]) == int(n[j + 1]):
            if e == -1:
                e = j
            p.append(int(n[j]))
        else:
            p.append(int(n[j]))
            e = -1
    for j in range(len(p)):
        P += p[j] * 10 ** (len(p) - j - 1)
    print("Case #{}: {}".format(i, P))
            
    