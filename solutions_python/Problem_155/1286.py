T = int(input())
i = 0
while i < T:
    line = input()
    line = line.split()
    Smax = int(line[0])
    audiencia = [int(i) for i in line[1]]
    miembros = 0
    amigos = 0
    j = 0
    while j <= Smax and miembros < Smax:
        if audiencia[j] == 0:
            pass
        else:
            if miembros >= j:
                miembros = miembros + audiencia[j]
            elif miembros < j:
                aux = j - miembros
                miembros = miembros + audiencia[j] + aux
                amigos = amigos + aux
        j += 1
    print("Case #" + str(i+1)+": " + str(amigos))
    i += 1

        
