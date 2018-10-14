def expandCake(cake):
    done=set()
    possible=[]
    for i in range(len(cake)):
        for j in range(len(cake[i])):
            if cake[i][j] != "?" and not cake[i][j] in done:
                done.add(cake[i][j])
                iMax=i
                iMin=i
                jMax=j
                jMin=j
                while iMin > 0 and cake[iMin-1][j]=="?":
                    iMin-=1
                while iMax < len(cake)-1 and cake[iMax+1][j]=="?":
                    iMax+=1
                while jMin > 0:
                    clear=True
                    for initial in range(iMin, iMax+1):
                        if cake[initial][jMin-1] != '?':
                            clear=False
                    if not clear:
                        break
                    else:
                        jMin-=1
                   
                while jMax < len(cake[i])-1:
                    clear=True
                    for initial in range(iMin, iMax+1):
                        if cake[initial][jMax+1] != '?':
                            clear=False
                    if not clear:
                        break
                    else:
                        jMax+=1
                possible.append(((iMax+1-iMin)*(jMax+1-jMin),cake[i][j], i, j))
    possible.sort()
    possible.reverse()
    for size, initial, i, j in possible:
        iMax=i
        iMin=i
        jMax=j
        jMin=j
        while iMin > 0 and cake[iMin-1][j]=="?":
            iMin-=1
        while iMax < len(cake)-1 and cake[iMax+1][j]=="?":
            iMax+=1
        while jMin > 0:
            clear=True
            for initial in range(iMin, iMax+1):
                if cake[initial][jMin-1] != '?':
                    clear=False
            if not clear:
                break
            else:
                jMin-=1
           
        while jMax < len(cake[i])-1:
            clear=True
            for initial in range(iMin, iMax+1):
                if cake[initial][jMax+1] != '?':
                    clear=False
            if not clear:
                break
            else:
                jMax+=1
        for mi in range(iMin, iMax+1):
            for mj in range(jMin, jMax+1):
                cake[mi][mj]=cake[i][j]
                        
    return cake

def main():
    t=int(input())
    for number in range(1, t + 1):
        R, C = input().split(" ")
        R = int(R)
        C = int(C)
        cake=[]
        for i in range(R):
            cake.append(list(input()))
        cake=expandCake(cake)
        print("Case #{}:".format(number))
        for line in cake:
            print("".join(line))
        
main()