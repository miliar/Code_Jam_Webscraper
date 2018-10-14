import math
from functools import reduce
import sys

fichierInput = open('input.in', 'r')
fichierOutput = open('output.out', 'w')
contenuFichier = fichierInput.read()
fichierInput.close()
lignes = contenuFichier.split("\n")
nbTests = int(lignes.pop(0))

resolutions = []

for unNumeroDeTest in range(0,nbTests):
    N,Q = [int(x) for x in lignes.pop(0).split(" ")]
    print("Voici N et Q",N,Q)
    horses = {}
    for i in range(1,N+1):
        E,S = [int(x) for x in lignes.pop(0).split(" ")]
        horses[i] = {"autonomie":E,"vitesse":S,"position":i}
    horses[N]["best"] = 0
    distances = {}
    for i in range(1,N+1):
        lesDistances = [int(x) for x in lignes.pop(0).split(" ")]
        lesDistances = {index+1:valeur for index,valeur in enumerate(lesDistances)}
        distances[i] = lesDistances

    for i in reversed(range(1,N)):
        vitesseDuCheval = horses[i]["vitesse"]
        bests = []
        autonomieRestante = horses[i]["autonomie"]
        totalParcouru = 0
        for j in range(i + 1,N+1):
            if autonomieRestante >= distances[j-1][j]:
                if horses[j]["best"] >= 0:
                    localBest = (totalParcouru + distances[j-1][j])/vitesseDuCheval + horses[j]["best"]
                    print("On est là",i,j,localBest)
                    bests.append(localBest)
            else:
                break
            autonomieRestante -= distances[j-1][j]
            totalParcouru = horses[i]["autonomie"] - autonomieRestante
        best = -1
        if len(bests) > 0:
            best = min(bests)
        horses[i]["best"] = best

    targets = []
    for i in range(0,Q):
        target = [int(x) for x in lignes.pop(0).split(" ")]
        targets.append({"depart":target[0],"arrivee":target[1]})

    resolution = horses[1]["best"]
    resolutions.append(str(resolution))

print(resolutions)

resolutions = ["Case #" + str(i) + ": " + valeur for i,valeur in enumerate(resolutions,start=1)]

resolutions = "\n".join(resolutions)

fichierOutput.write(resolutions)
fichierOutput.close()