fin = open("input.txt", "r")
fout = open("output.txt", "w")

def gcd(a, b):
    while (a > 0 and b > 0):
        if (a > b):
            a %= b
        else:
            b %= a
    return (a + b)

t = int(fin.readline())

for i in range(t):
    st = fin.readline()
    a = [int(x) for x in st.split()]
    n = a[0]
    a = a[1 : n + 1]
    a.sort()
    a.reverse()

    q = a[0] - a[1]
    for j in range(n - 1):
        q = gcd(q, a[j] - a[j + 1])
    if a[0] % q == 0:
        y = 0
    else:
        y = q - a[0] % q
    fout.write("Case #" + str(i + 1) + ": " + str(y) + "\n")

fin.close()
fout.close()