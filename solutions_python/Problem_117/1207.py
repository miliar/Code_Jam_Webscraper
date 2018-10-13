def check(grass,m,n):
    rmax = []
    cmax = []
    for i in range(m):
        row = grass[i*n:i*n + n]
        rmax.append(max(row))
        print(row)

    for i in range(n):
        col = grass[i::n]
        cmax.append(max(col))

    for i in range(n):
        for j in range(m):
            if grass[j*n + i] < min(rmax[j],cmax[i]):
                return "NO"

    return "YES"

f_in = open("input.txt")
f_out = open("output.txt","+w")
n_cases = int(f_in.readline())
case = 0
while(case<n_cases):
    case += 1
    m, n = (int(x) for x in f_in.readline().split())
    grass = []
    for i in range(m):
        grass.extend((int(x) for x in f_in.readline().split()))

    ans = check(grass,m,n)
    print("Case #" + str(case) + ": " + ans)
    f_out.write("Case #" + str(case) + ": " + ans +"\n")

f_in.close()
f_out.close()
