def simulate(n, k):
    posedeni = [0, n+1]
    for i in range(k):
        SL = -1
        SR = -1
        indeks = None
        tag = None
        for j in range(len(posedeni) - 1):
            razlika = posedeni[j+1] - posedeni[j] - 1
            if razlika > 0:
                L = (razlika - 1)//2
                R = razlika - 1 - L
                if min(L,R) > min(SL,SR):
                    SL = L
                    SR = R
                    indeks = j
                    tag = posedeni[j] + L + 1
                elif min(L,R) == min(SL,SR):
                    if max(L,R) > max(SL,SR):
                        SL = L
                        SR = R
                        indeks = j
                        tag = posedeni[j] + L + 1
                else:
                    pass
        posedeni = posedeni[:indeks+1] + [tag] + posedeni[indeks+1:]
    return max(SL,SR), min(SL,SR)

T = int(input().strip())

f = open('bathroom.txt', 'w')

for C in range(1, T + 1):
    n, k = input().strip().split()
    n, k = int(n), int(k)
    m, M = simulate(n,k)
    print(C, 'DONE', m, M)
    f.write('Case #{0}: {1} {2} \n'.format(C,m,M))
f.close()

            
