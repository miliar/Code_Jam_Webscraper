import sys

file = open(sys.argv[1])
case = int(file.readline())

def check_toto(j, k, grid, N, M):
        value = grid[j][k]
        for k1 in range(M):
                if value < grid[j][k1]:
                        for j1 in range(N):
                                if value < grid[j1][k]:
                                        return 0

        return 1

for i in range(case):
        grid = []
        N, M = map(int, file.readline().split())

        # create grid
        for j in range(N):
                l1 = map(int, file.readline().split())
                grid.append(l1)


        ok = 1
        # trouver un moyen de save la derniere bigger value
        for j in range(N):
                for k in range(M):
                        # check si c'est la plus grande valeur en ligne et colone
                        ok = check_toto(j, k, grid, N, M)

                        if ok == 0:
                                break
                if ok == 0:
                        break

        if ok == 0:
                print("Case #%d: NO") % (i+1)
        else:
                print("Case #%d: YES") % (i+1)
                                


