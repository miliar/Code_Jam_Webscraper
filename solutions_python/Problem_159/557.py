cases = int(input())
for casecounter in range(cases):
    tam = int(input())
    mush = [int(i) for i in input().split()]
    caso1 = 0
    velocidad = [0]
    for count in range(len(mush) - 1):
        if mush[count] > mush[count + 1]:
            caso1 += mush[count] - mush[count+1]
        if mush[count] > mush[count + 1]:
            dif = mush[count] - mush[count+1]
            velocidad.append(dif/10)
    velocidad = max(velocidad)
    caso2 = 0
    for count in range(len(mush) - 1):
        caso2 += min(mush[count],velocidad*10)
    print("Case #" + str(casecounter+1) + ": " + str(int(caso1)) + ' ' + str(int(caso2)))
