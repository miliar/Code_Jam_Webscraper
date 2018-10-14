testcase = int(input())

def check(arr, startx, endx, starty, endy, exceptchar):
    #status = True
    #print("CHECK", startx, starty, endx, endy)
    for i in range(startx, endx+1):
        for j in range(starty, endy+1):
            #print(arr[i][j])
            if arr[i][j] not in ('?', exceptchar):
                return False
    return True

for tc in range(1, testcase+1):
    linestr = input().split(" ")
    R = int(linestr[0])
    C = int(linestr[1])
    cakegrid = []
    alphaloc = {}
    for i in range(R):
        temp = input()
        cakegrid.append([])
        for j in range(len(temp)):
            cakegrid[i].append(temp[j])
            if temp[j] in alphaloc and temp[j] != '?':
                continue
                #print("ERROR "+temp[j])
                #alphaloc[temp[j]].append( (i, j) )
                #raise Exception
            elif temp[j] != '?':
                #alphaloc[temp[j]] = [(i, j)]
                alphaloc[temp[j]] = (i, j)
    #print(cakegrid)

    completed = []
    for i in range(R):
        for j in range(C):
            if cakegrid[i][j] != '?' and cakegrid[i][j] not in completed:
                startx, endx = i, i
                starty, endy = j, j

                #print(cakegrid[i][j])
                #while startx >= 0 and cakegrid[startx][j] == '?':

                while startx >= 0 and starty >= 0 and check(cakegrid, startx, endx, starty, endy, cakegrid[i][j]):
                    startx -=1
                    starty -=1
                    #print(startx, starty)
                startx += 1
                starty += 1
                
                while startx >= 0 and check(cakegrid, startx, endx, starty, endy, cakegrid[i][j]):
                    startx -=1
                startx +=1
                #if startx < 0:
                #    startx = 0

                while starty >= 0 and check(cakegrid, startx, endx, starty, endy, cakegrid[i][j]):
                    starty-=1
                starty+=1
                #if starty < 0:
                #    startx = 0

                while endx < R and endy < C and check(cakegrid, startx, endx, starty, endy, cakegrid[i][j]):
                    #print(cakegrid[endx][endy])
                    endx +=1
                    endy +=1
                    #print(endx, endy)
                endx -= 1
                endy -= 1

                while endx < R and check(cakegrid, startx, endx, starty, endy, cakegrid[i][j]):
                    endx+=1
                endx-=1

                while endy < C and check(cakegrid, startx, endx, starty, endy, cakegrid[i][j]):
                    endy+=1
                endy-=1

                completed.append(cakegrid[i][j])
                #print(startx, starty, endx, endy)
                for i1 in range(startx, endx+1):
                    for j1 in range(starty, endy+1):
                        cakegrid[i1][j1] = cakegrid[i][j]

                #print("dd")
                #print(cakegrid)

    print("Case #"+str(tc)+":")
    for i in range(R):
        anstempstr = ""
        for j in range(C):
            anstempstr += cakegrid[i][j]
        print(anstempstr)
                    

                
