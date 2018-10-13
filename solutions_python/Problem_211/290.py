input = open('C-small-1-attempt0.in', 'r')
output = open('C-small-1-attempt0.out', 'w')
t = int(input.readline().rstrip())
for test in range(t):
    output.write("Case #" + str(test + 1) + ": ")
    n, k = map(int, input.readline().rstrip().split())
    u = float(input.readline().rstrip())
    p = sorted(list(map(float, input.readline().rstrip().split()))) + [1]
    i = 0
    while i < n and u >= (p[i + 1] - p[i]) * (i + 1):
        u -= (p[i + 1] - p[i]) * (i + 1)
        p[i] = p[i+1]
        i += 1
    if u > 0 and p[i] < 1:
        p[i] += u / (i + 1)
    p_res = p[i] ** (i+1)
    for j in range (i+1, n):
        p_res *= p[j]
    print(p_res, file = output)
    
input.close()
output.close()