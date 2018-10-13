with open("A-large.in", "r") as inp:
    with open("A-large.out", "w") as outp:
        cases = int(inp.readline())
        for i in range(cases):
            rows, columns = [int(k) for k in inp.readline().split()]
            cake = []
            columnwise = False
            for j in range(rows):
                row = inp.readline().strip()
                if row == "?" * len(row):
                    columnwise = True
                cake.append(list(row))
            it = rows
            nit = columns
            if columnwise:
                cake = [list(r) for r in zip(*cake)]
                it = columns
                nit = rows
            cont = True
            while cont:
                cont = False
                for j in range(it):
                    for el in range(nit):
                        if cake[j][el] != "?":
                            k = el - 1
                            while k >= 0:
                                if cake[j][k] != "?":
                                    break
                                cake[j][k] = cake[j][el]
                                k -= 1
                            k = el + 1
                            while k < nit:
                                if cake[j][k] != "?":
                                    break
                                cake[j][k] = cake[j][el]
                                k += 1
                    if "?" in cake[j]:
                        cont = True
                if cont:
                    cake = [list(r) for r in zip(*cake)]
                    prov = it
                    it = nit
                    nit = prov
                    columnwise = not columnwise
            if columnwise:
                cake = [list(r) for r in zip(*cake)]
            outp.write("Case #" + str(i+1) + ":\n")
            for j in range(rows):
                outp.write("".join(cake[j]) + "\n")
