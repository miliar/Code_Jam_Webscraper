# file = open("B-small-attempt0.in", "r")
# t = int(file.readline().strip("\n"))
t = int(input().strip())
# file_out = open("output.out", "w")

def distanza(inizio, fine):
    if fine < inizio: fine += 1440
    return fine - inizio

risultato = ""
for m in range(t):
    # c, j = [int(x) for x in file.readline().strip("\n").split(" ")]
    c, j = [int(x) for x in input().strip().split(" ")]
    ini_c, fine_c, ini_j, fine_j = [], [], [], []
    for i in range(c):
        # x, y = [int(x) for x in file.readline().strip("\n").split(" ")]
        x, y = [int(x) for x in input().strip().split(" ")]
        ini_c.append(x)
        fine_c.append(y)
    for i in range(j):
        # x, y = [int(x) for x in file.readline().strip("\n").split(" ")]
        x, y = [int(x) for x in input().strip().split(" ")]
        ini_j.append(x)
        fine_j.append(y)
    minimo = 0
    if c <= 1 and j <= 1:
        minimo = 2
    elif c == 2:
        if distanza(ini_c[0], fine_c[1]) <= 720 or distanza(ini_c[1], fine_c[0]) <= 720: minimo = 2
        else: minimo = 4
    else:
        if distanza(ini_j[0], fine_j[1]) <= 720 or distanza(ini_j[1], fine_j[0]) <= 720: minimo = 2
        else: minimo = 4
    risultato += "Case #" + str(m + 1) + ": " + str(minimo) + ("\n" if m != t - 1 else "")
    
print(risultato)
# file_out.write(risultato)
# file_out.close()
