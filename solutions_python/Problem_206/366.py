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
    D,N = [int(x) for x in lignes.pop(0).split(" ")]
    horses = []
    for i in range(0,N):
        position,vitesse = [int(x) for x in lignes.pop(0).split(" ")]

        horses.append({"position":position,"vitesse":vitesse,"id":i,"temps":(D - position)/vitesse})

    tempsRetenu = max([horse["temps"] for horse in horses])

    resolution = D / tempsRetenu
    resolutions.append(str(resolution))

print(resolutions)

resolutions = ["Case #" + str(i) + ": " + valeur for i,valeur in enumerate(resolutions,start=1)]

resolutions = "\n".join(resolutions)

fichierOutput.write(resolutions)
fichierOutput.close()