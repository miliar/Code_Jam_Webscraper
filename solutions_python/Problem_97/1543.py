fi = open("input.txt", "r")
fo = open("output.txt", "w")

t = int(fi.readline().strip())

for tests in range(t):
    a, b = map(int, fi.readline().split())
    ans = 0
    for n in range(a, b + 1):
        m = -1
        cur = 1
        while m != n:
            x = int("1" + "0"*cur)
            m = str(n%x)
            if str(n//x) != "0":
                m += str(n//x)
            m = int(m) 
            if m != n and a <= m <= b:
                ans += 1
            cur += 1
            #print (n, m)
    fo.write("Case #%d: " % (tests + 1) + str(ans//2) + "\n")