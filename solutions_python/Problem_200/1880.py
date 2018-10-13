def tidy(n):
    k = str(n)
    for i in range(len(k) - 1):
        if k[i] > k[i+1]:
            return False
    return True

def find(n):
    if tidy(n):
        return n
    else:
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
                zac = n[:i+1]
                kon = n[i+1:]
                zac = str(int(zac)-1)
                for _ in kon:
                    zac += '9'
                return find(str(int(zac)))

f = open('tatbig.txt', 'w')

T = int(input().strip())

for C in range(1, T + 1):
    a = input().strip()
    x = find(a)
    print(a, x)
    f.write('Case #{0}: {1}\n'.format(C, x))
f.close()
