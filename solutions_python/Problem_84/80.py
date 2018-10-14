def solve(tab, row, col):
    i = 0
    while i < row:
        j = 0
        while j < col:
            if tab[i][j] == "#":
                if col - j > 1 and row - i > 1 and tab[i+1][j] == "#" and tab[i][j+1] == '#' and tab[i+1][j+1] == '#':
                    tab[i][j] = '/'
                    tab[i+1][j] = "\\"
                    tab[i][j+1] = "\\"
                    tab[i+1][j+1] = '/'
                else:
                    return False
            j+=1
        i+=1

    return tab

n_tests = int(input())
for t in range(0, n_tests):
    row, col = [ int(i) for i in input().split(" ") ]
    
    tab = []
    for line in range(0, row):
        sline = input()
        
        tab.append([c for c in sline[0:col] ])

    print ("Case #"+str(t+1)+": ")
    r = solve(tab, row, col)
    if r:    
        for l in solve(tab, row, col):
            print ("".join(l))
    else:
        print ("Impossible")

    