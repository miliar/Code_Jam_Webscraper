
def solve(cavalli_data, destination):
    tempi_fine = []
    for cavallo in cavalli_data:
        distanza_mancante = destination - cavallo["p"]
        assert distanza_mancante >= 0, distanza_mancante
        tempo_fine = float(distanza_mancante) / cavallo["v"]
        tempi_fine.append(tempo_fine)
    max_tempo_fine = max(tempi_fine)
    max_vel = float(destination) / max_tempo_fine
    return max_vel




risultati = []
with open("A-large.in") as f:
    t = int(f.readline())
    print "t", t
    for i in range(t):
        d, n = (int(v) for v in f.readline().strip().split(" "))
        print "n, d", n, d, i
        dati_cavalli = []
        for j in range(n):
            row = f.readline().strip().split(" ")
            partenza = int(row[0])
            velocita = int(row[1])
            dati_cavalli.append({"p": partenza, "v": velocita})
        # print row
        risultati.append(solve(dati_cavalli, d))

with open("outLarge.txt", "w") as out:
    for i, r in enumerate(risultati):
        out.write("Case #{}: {}\n".format(i+1, r))