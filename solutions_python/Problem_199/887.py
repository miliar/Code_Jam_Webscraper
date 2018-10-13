def voltearPancakes(S, K, posicion):
    listS = list(S)
    for i in range(K):
        if listS[i + posicion] == "+":
            listS[i + posicion] = "-"
        else:
            listS[i + posicion] = "+"
    return "".join(map(str, listS))

T = int(input())
for i in range(1, T + 1):
    entrada = input().split(" ")
    S = entrada[0]
    K = int(entrada[1])

    cantidad = 0
    posicion = 0
    final = False
    while not final:
        if S[posicion] == "-":
            S = voltearPancakes(S, K, posicion)
            cantidad = cantidad + 1

        posicion = posicion + 1

        if posicion > len(S) - K:
            final = True

    if S == "+" * len(S):
        salida = str(cantidad)
    else:
        salida = "IMPOSSIBLE"

    print("Case #{}: {}".format(i, salida))
