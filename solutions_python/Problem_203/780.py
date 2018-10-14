import sys, copy

def fix_blanks(cake):
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            prevrow = i > 0
            nextrow = i < rows-1
            prevcol = j > 0
            nextcol = j < cols-1
            if cake[i][j] != '?':
                j += 1
                continue
            if prevrow and prevcol and cake[i-1][j] != '?' \
            and cake[i-1][j-1] == cake[i-1][j] == cake[i][j-1]:
                cake[i][j] = cake[i-1][j-1]
            elif prevrow and cake[i-1][j] != '?' \
            and (not prevcol or cake[i-1][j-1] != cake[i-1][j]
                 or cake[i][j] == cake[i][j-1]) \
            and (not nextcol or cake[i-1][j] != cake[i-1][j+1]
                 or cake[i][j] == cake[i][j+1]):
                cake[i][j] = cake[i-1][j]
                if prevcol and cake[i-1][j-1] == cake[i-1][j]:
                    cake[i][j-1] = cake[i-1][j-1]
                if nextcol and cake[i-1][j+1] == cake[i-1][j]:
                    cake[i][j+1] = cake[i-1][j+1]

            elif nextrow and cake[i+1][j] != '?' \
            and (not prevcol or cake[i+1][j-1] != cake[i+1][j]
                 or cake[i][j] == cake[i][j-1]) \
            and (not nextcol or cake[i+1][j] != cake[i+1][j+1]
                 or cake[i][j] == cake[i][j+1]):
                cake[i][j] = cake[i+1][j]
                if prevcol and cake[i+1][j-1] == cake[i+1][j]:
                    cake[i][j-1] = cake[i+1][j-1]
                if nextcol and cake[i+1][j+1] == cake[i+1][j]:
                    cake[i][j+1] = cake[i+1][j+1]

            elif prevcol and cake[i][j-1] != '?' \
            and (not nextrow or cake[i][j-1] != cake[i+1][j-1]
                 or cake[i][j] == cake[i+1][j]) \
            and (not prevrow or cake[i][j-1] != cake[i-1][j-1] 
                 or cake[i][j] == cake[i-1][j]):
                cake[i][j] = cake[i][j-1]
                if nextrow and cake[i+1][j-1] == cake[i][j-1]:
                    cake[i+1][j] = cake[i+1][j-1]
                if prevrow and cake[i-1][j-1] == cake[i][j-1]:
                    cake[i-1][j] = cake[i-1][j-1]

            elif nextcol and cake[i][j+1] != '?' \
            and (not nextrow or cake[i][j+1] != cake[i+1][j+1]
                 or cake[i][j] == cake[i+1][j]) \
            and (not prevrow or cake[i][j+1] != cake[i-1][j+1] 
                 or cake[i][j] == cake[i-1][j]):
                cake[i][j] = cake[i][j+1]
                if nextrow and cake[i+1][j+1] == cake[i][j+1]:
                    cake[i+1][j] = cake[i+1][j+1]
                if prevrow and cake[i-1][j+1] == cake[i][j+1]:
                    cake[i-1][j] = cake[i-1][j+1]
            j += 1
        i += 1
    return cake

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for case in xrange(1,cases+1):
    print "Case #" + str(case) + ":"
    rows, cols = [int(x) for x in stdin.pop(0).strip().split()]
    cake = []
    for row in xrange(rows):
        cake.append(list(stdin.pop(0).strip()))
    blanks = False
    for row in cake:
        if '?' in row:
            blanks = True
            break
    # count = 0
    while blanks:
        # oldcake = copy.copy(cake)
        cake = fix_blanks(cake)
        # if oldcake == cake:
        #     count += 1
        #     if count == 5:
        #         break
        blanks = False
        for row in cake:
            if '?' in row:
                blanks = True
                break
    for row in cake:
        print ''.join(row)
