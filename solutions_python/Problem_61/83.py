f = open("data.txt")
g = open("data1.txt", 'w')

def pure(s, n):
    if s[0] == n:
        return 1
    elif (s.index(n)+1) not in s:
        return 0
    else:
        u = (s.index(n)+1)
        return pure(s, u)
def count(n):
    c = 0
    for r in range(0, 2**(n-2)):
        s = []
        w = list(bin(r))
        w.reverse()
        for j in range(len(w)-2):
             if int(w[j]) == 1:
                 s.append(j + 2)
        s.append(n)
        c += pure(s, n)
    return(c)

vec = [0, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 140268, 268066, 513350, 984911]

for i, line in enumerate(f):
    if i == 0:
            continue
    n = int(line.split()[0])
    stri = str(vec[n-1]%100003)
    string = 'Case #' + str(i) + ': ' + stri + '\n'
    g.write(string)
    print(string)
