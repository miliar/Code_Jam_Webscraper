import copy

def main():
    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        print("Case #{}: ".format(case))
        r, c = [int(x) for x in input().split(" ")]
        map = []
        for i in range(r):
            map.append(list(input()))
        newmap = copy.deepcopy(map)
        for i in range(r):
            for j in range(c):
                if map[i][j] != '?':
                    low = j
                    high = j
                    for k in range(j-1, -1, -1):
                        if newmap[i][k] == '?':
                            low = k
                            newmap[i][k] = map[i][j]
                        else:
                            break
                    for l in range(j+1, c):
                        if newmap[i][l] == '?':
                            high = l
                            newmap[i][l] = map[i][j]
                        else:
                            break
                    found = False
                    for k in range(i - 1, -1, -1):
                        for m in range(low, high + 1):
                            if newmap[k][m] != '?':
                                found = True
                                break
                        if found:
                            break
                        for m in range(low, high + 1):
                            newmap[k][m] = map[i][j]

                    found = False
                    for l in range(i + 1, r):
                        for m in range(low, high + 1):
                            if newmap[l][m] != '?':
                                found = True
                                break
                        if found:
                            break
                        for m in range(low, high + 1):
                            newmap[l][m] = map[i][j]
        for line in newmap:
            print(''.join(line))

if __name__ == '__main__':
    main()