t = int(input().strip())

risultato = ""
for i in range(t):
    n = [int(x) for x in input().strip()]
    fine = False
    while not fine:
        fine = True
        if n[0] == 0:
            n = [9 for x in range(len(n)-1)]
        else:
            for j in range(len(n)-1):
                if n[j+1] < n[j]:
                    n = n[:j] + [n[j]-1] + [9 for x in range(len(n)-j-1)]
                    fine = False

    risultato += "Case #" + str(i + 1) + ": " + "".join(map(str, n)) + ("\n" if i != t - 1 else "")

print(risultato)
