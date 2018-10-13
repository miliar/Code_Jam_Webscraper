t = int(input().strip())

risultato = ""
for i in range(t):
    n, k = [int(x) for x in input().strip().split(" ")]
    livello = dict()
    # ripetizioni
    livello["rip"] = 1
    # risultati
    livello["ris"] = [n//2, n//2-1 if n % 2 == 0 else n//2]
    pila_livelli = [dict(livello)]
    indice = 0
    totale = 1
    while totale < k and livello["ris"] != [0, 0]:
        precedenti = pila_livelli[indice]["ris"][:]
        livello["rip"] = pila_livelli[indice]["rip"]
        if precedenti[0] == precedenti[1]:
            precedenti.pop()
            livello["rip"] *= 2
        for x in precedenti:
            if totale < k and x != 0:                
                livello["ris"] = [x//2, x//2-1 if x % 2 == 0 else x//2]
                if pila_livelli[-1]["ris"] == livello["ris"]: pila_livelli[-1]["rip"] += livello["rip"]
                else: pila_livelli.append(dict(livello))
                totale += livello["rip"]
        indice += 1
    risultato += "Case #" + str(i + 1) + ": " + " ".join(map(str, pila_livelli[-1]["ris"])) + ("\n" if i != t - 1 else "")

print(risultato)
