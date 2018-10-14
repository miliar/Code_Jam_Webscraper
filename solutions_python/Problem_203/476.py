ret = []
with open('A-large.in', 'r') as file:
    t = int(file.readline())
    for __ in range(t):
        r, c = map(int, file.readline().split())
        cake = []
        for row in range(r):
            cake.append(file.readline().strip())

        letters = set()

        rowlo = {}
        rowhi = {}
        collo = {}
        colhi = {}

        for i, row in enumerate(cake):
            for j, let in enumerate(row):
                if let != '?':
                    letters.add(let)
                    if let in rowlo:
                        if i < rowlo[let]:
                            rowlo[let] = i
                        if i > rowhi[let]:
                            rowhi[let] = i
                        if j < collo[let]:
                            collo[let] = j
                        if j > colhi[let]:
                            colhi[let] = j
                    else:
                        rowlo[let] = i
                        rowhi[let] = i
                        collo[let] = j
                        colhi[let] = j

        print(rowlo)
        print(rowhi)
        print(collo)
        print(colhi)
        print(r, c)
        output = [[0] * c for _ in range(r)]

        for let in letters:
            for i in range(rowlo[let], rowhi[let]+1):
                for j in range(collo[let], colhi[let]+1):
                    output[i][j] = let
        change = True
        while change:
            change = False
            #rowsearch
            for d in [-1, 1]:
                for let in letters:
                    if d == -1:
                        for i in range(rowlo[let]-1, -1, -1):
                            block = False
                            for j in range(collo[let], colhi[let]+1):
                                # print('row-', let, i, j)
                                if output[i][j]:
                                    block = True
                            if not block:
                                for j in range(collo[let], colhi[let] + 1):
                                    output[i][j] = let
                                rowlo[let] = i
                                change = True
                            else:
                                break

                    if d == 1:
                        for i in range(rowhi[let]+1, r):
                            block = False
                            for j in range(collo[let], colhi[let] + 1):
                                # print('row+', let, i, j)
                                if output[i][j]:
                                    block = True
                            if not block:
                                for j in range(collo[let], colhi[let] + 1):
                                    output[i][j] = let
                                rowhi[let] = i
                                change = True
                            else:
                                break
            #colsearch
            for d in [-1, 1]:
                for let in letters:
                    if d == -1:
                        for j in range(collo[let]-1, -1, -1):
                            block = False
                            for i in range(rowlo[let], rowhi[let]+1):
                                # print('col', let, i, j)
                                if output[i][j]:
                                    block = True
                            if not block:
                                for i in range(rowlo[let], rowhi[let]+1):
                                    output[i][j] = let
                                collo[let] = j
                                change = True
                            else:
                                break
                    if d == 1:
                        for j in range(colhi[let]+1, c):
                            block = False
                            for i in range(rowlo[let], rowhi[let]+1):
                                if output[i][j]:
                                    block = True
                            if not block:
                                for i in range(rowlo[let], rowhi[let]+1):
                                    output[i][j] = let
                                colhi[let] = j
                                change = True
                            else:
                                break

        print(output)
        tret = "\n"
        for row in output:
            tret += ''.join(row)
            tret += "\n"
        ret.append(tret)

with open('Aout-large.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s" %(i+1, ret[i]))