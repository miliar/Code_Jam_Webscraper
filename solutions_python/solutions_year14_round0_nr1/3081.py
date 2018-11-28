f = open("Output.txt", "w")
cazul = 1
grid_initial = False
liniaDinGridul2 = 1
i = 0#numara liniile
for e in open("Input.txt", "r"):
    if i != 0:
        if (i - 1) % 5 == 0:#citesc linia pe care e cartea cautata
            linie_cautata = int(e)
            linie = 1
            if(grid_initial):
                grid_initial = False
            else:
                grid_initial = True
        else:
            if grid_initial:
                if linie == linie_cautata:
                    a = [int(zz) for zz in e.split()]
            else:#gridul rearanjat
                if liniaDinGridul2 > 4:
                    liniaDinGridul2 = 1
                if liniaDinGridul2 == linie_cautata:
                    cate = 0
                    for c in a:
                        if c in [int(z) for z in e.split()]:
                            cate += 1
                    if cate == 0:
                        f.write("Case #" + str(cazul) + ": " + "Volunteer cheated!\n")
                    if cate not in (0, 1):
                        f.write("Case #" + str(cazul) + ": " + "Bad magician!\n")
                    if cate == 1:
                        for c in a:
                            if c in [int(z) for z in e.split()]:
                                gasit = c
                        f.write("Case #" + str(cazul) + ": " + str(gasit) + "\n")
                    cazul += 1
                liniaDinGridul2 += 1
            linie += 1
    i += 1
f.close()
