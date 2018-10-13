import math

for i in range(int(input())):
    c = 0
    m, M = map(int, input().split(' '))
    cm = math.floor(math.sqrt(m))
    CM = math.ceil(math.sqrt(M))


    for j in range(cm, CM + 1):
        if str(j) == str(j)[::-1]:
            carre = j*j
            if m <= carre <= M and str(carre) == str(carre)[::-1]:
                c += 1
    
    print("Case #%s: %s" % (i + 1, c))
