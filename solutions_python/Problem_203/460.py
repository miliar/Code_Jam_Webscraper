T = input()
# global
R,C = None,None
data = []

def isLegal(i,j):
    if i<0 or i>=R:
        return False
    if j <0 or j>=C:
        return False
    return data[i][j] != '?'

ctr = 0
# print "G"
while ctr < T:
    ctr+=1
    # print "G",_
    data = []
    R, C = map(int,raw_input().split())
    for _ in range(R):
        data.append(list(raw_input()))

   

    fill = -1
    newfill = 0
    while fill != newfill:
        fill = newfill
        # print data,fill,newfill
        for i in range(R):
            for j in range(C):
                if data[i][j] == '?':
                    # FROM LEFT
                    if isLegal(i,j-1):
                        data[i][j] = data[i][j-1]
                        newfill+=1

                    #FROM RIGHT
                    elif isLegal(i,j+1):
                        data[i][j] = data[i][j+1]
                        newfill+=1

    fill = -1
    newfill = 0
    while fill != newfill:
        fill = newfill
        # print data,fill,newfill
        for i in range(R):
            for j in range(C):
                if data[i][j] == '?':
                    # UP
                    if isLegal(i-1,j):
                        data[i][j] = data[i-1][j]
                        newfill+=1
                    elif isLegal(i+1,j):
                        data[i][j] = data[i+1][j]
                        newfill+=1
                        # # count how many 
                        # count = 1
                        # done = True
                        # ci = 1
                        # while True:
                        #     if j+ci == j+ci-1:
                        #         count +=1
                        #     else:
                        #         done = False

                        # do we have the same count available freel



                    #DOWN

                    

    # LEFT, RIGHT exhausted.
    # PRINT data
    print "Case #"+str(ctr)+": "
    for j in data:
        print ''.join(j)

    # print data
    # _+=1