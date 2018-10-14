t = int(input())  # read a line with a single integer
for k in range(1, t + 1):
    R, C = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    mat = []
    for i in range(0, R):
        mat.append(list(input()))
    i = 0
    j = 0
    # beforeI = 0
    letters = []
    while i < R:
        # ifI = False
        j = 0
        while True:
            if j >= C:
                i += 1
                # if not ifI:
                #   beforeI += 1
                break
            else:
                if mat[i][j] != '?':
                    # ifI = True
                    letter = mat[i][j]
                    if letter in letters:
                        j += 1
                    else:
                        letters.append(letter)
                        # for wesh in range(0, beforeI + 1):
                        #    for t in range(0, beforeJ + 1):
                        #        mat[i-wesh][j-t] = letter
                        beforeJ = j
                        beforeI = i
                        while beforeJ > 0:
                            if mat[i][beforeJ - 1] == '?':
                                beforeJ -= 1
                                mat[i][beforeJ] = letter
                            else:
                                break
                        while beforeI > 0:
                            if all(l == '?' for l in mat[beforeI - 1][beforeJ:j + 1]):
                                beforeI -= 1
                                for lol in range(beforeJ, j + 1):
                                    mat[beforeI][lol] = letter
                            else:
                                break
                        tempJ = j
                        while tempJ < C - 1:
                            temp = list(l for l in (mat[i][tempJ + 1]) for tos in range(beforeI, i+1))
                            if all(l == '?' for l in temp):
                                tempJ += 1
                                for lol in range(beforeI, i+1):
                                    mat[lol][tempJ] = letter
                            else:
                                break
                        tempI = i
                        while tempI < R - 1:
                            if all(l == '?' for l in mat[tempI + 1][beforeJ:tempJ + 1]):
                                tempI += 1
                                for lol in range(beforeJ, tempJ + 1):
                                    mat[tempI][lol] = letter
                            else:
                                break
                        j = tempJ
                        # beforeI = 0
                        # beforeJ = 0
                else:
                    # beforeJ += 1
                    j += 1
    print("Case #{}:".format(k))
    for l in mat:
        print("".join(l))
    print("")
