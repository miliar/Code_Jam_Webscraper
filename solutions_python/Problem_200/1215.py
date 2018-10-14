def tidy(n):
    a = list(str(n))
    if len(a)>=2:
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i] = str(int(a[i])-1)
                for j in range(i+1, len(a)):
                    a[j] = '9'

    a = ''.join(a)
    out = int(a)
    return out

def check_tidy(n):
    a = tidy(n)
    b = list(str(a))
    b.sort()
    b = ''.join(b)
    b = int(b)
    if a == b:
        return a
    else:
        return check_tidy(a)

in_f = open("i.in", 'r')
ou_f = open("o.out", 'w')

T = int(in_f.readline())
for i in range(T):
    s = in_f.readline().strip()
    k = int(s)
    out = check_tidy(k)

    j = "Case #" + str(i+1) +": " + str(out) + "\n"
    ou_f.write(j)
in_f.close()
ou_f.close()