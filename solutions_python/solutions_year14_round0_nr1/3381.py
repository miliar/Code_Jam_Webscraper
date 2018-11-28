f = open("input.in")
o = open("out.txt", 'w')
n = int(f.readline())
for j in range(n):
    m = int(f.readline())
    a = []
    for i in range(4):
        a.append(map(int, f.readline().split()))
    b = a[m-1]
    m = int(f.readline())
    a = []
    for i in range(4):
        a.append(map(int, f.readline().split()))
    c = a[m-1]
    s = set(b) & set(c)
    o.write("Case #{}: ".format(j+1))
    if len(s) == 1:
        o.write(str(list(s)[0]) + "\n")
    elif len(s):
        o.write("Bad magician!\n")
    else:
        o.write("Volunteer cheated!\n")

