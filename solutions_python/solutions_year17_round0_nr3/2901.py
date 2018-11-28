def checkFree(list, pos):
    rs = 0
    for i in list[pos + 1:]:
        if i == 0:
            rs += 1
        else:
            break
    ls = 0
    for i in reversed(list[:pos]):
        if i == 0:
            ls += 1
        else:
            break
    return (ls,rs)

with open('C-small-1-attempt0.in', 'r') as f:
    cases = int(f.readline())
    for n in range(cases):
        line = f.readline().split()
        stalls = int(line[0])
        people = int(line[1])
        if stalls == people:
            last = [0, 0]
        elif people == 1:
            if stalls%2 == 0:
                a = 1
            else:
                a = 0
            last = [int(stalls/2), int(stalls/2)-a]
        else:
            stallList = [1]
            for i in range(stalls):
                stallList.append(0)
            stallList.append(1)

            # print(stallList)
            for p in range(people):
                possibilities = []
                last = [0, 0]
                for s in range(len(stallList) - 2):
                    if stallList[s + 1] == 0:
                        (ls, rs) = checkFree(stallList, s + 1)
                        # print((ls,rs))
                        possibilities.append((ls,rs))
                    else:
                        possibilities.append((-999999,-999999))
                # print(possibilities)

                l = [min(x) for x in (possibilities)]
                m = max(l)
                l = [i for i, n in enumerate(l) if n == m]
                # print(l)
                if len(l) > 1:
                    l2 = [possibilities[x] for x in l]
                    l = [max(x) for x in l2]
                    m = max(l)
                    l = [i for i, n in enumerate(l) if n == m]
                    # print(l)
                    index = possibilities.index(l2[l[0]])+1
                    stallList[index] = 1
                    # print(possibilities[index-1])
                    last = [max(possibilities[index-1]), min(possibilities[index-1])]
                else:
                    index = l[0]+1
                    stallList[index] = 1
                    # print(possibilities[index - 1])
                    last = [max(possibilities[index-1]),min(possibilities[index-1])]
                # print(stallList)




        g = open('B-large.out', 'a')
        g.write("Case #%s: %s %s\n" % (n+1, last[0], last[1]))
        g.close()




f.close()