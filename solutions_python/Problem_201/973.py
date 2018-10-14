import math



def getDistances(people, stalls):
    #in the form (stall distance, stalls like it left)
    stallInfo=[[stalls, 1]]
    while people > stallInfo[0][1]:
        if stallInfo[0][0] % 2 == 0:
            adding=math.ceil((stallInfo[0][0]-1)/2)
            needed=-1
            for i in range(len(stallInfo)):
                if stallInfo[i][0] == adding:
                    needed=i
                    break
            if needed==-1:
                stallInfo.append([math.ceil((stallInfo[0][0]-1)/2), stallInfo[0][1]])
            else:
                stallInfo[needed][1]+=stallInfo[0][1]
            
            adding=math.floor((stallInfo[0][0]-1)/2)
            needed=-1
            for i in range(len(stallInfo)):
                if stallInfo[i][0] == adding:
                    needed=i
                    break
            if needed==-1:
                stallInfo.append([math.floor((stallInfo[0][0]-1)/2), stallInfo[0][1]])
            else:
                stallInfo[needed][1]+=stallInfo[0][1]
            
        else:
            adding=(stallInfo[0][0]-1)/2
            needed=-1
            for i in range(len(stallInfo)):
                if stallInfo[i][0] == adding:
                    needed=i
                    break
            if needed==-1:
                stallInfo.append([(stallInfo[0][0]-1)/2, stallInfo[0][1]*2])
            else:
                stallInfo[needed][1]+=stallInfo[0][1]*2
        people-=stallInfo[0][1]
        del stallInfo[0]
        stallInfo.sort()
        stallInfo.reverse()
    return (math.ceil((stallInfo[0][0]-1)/2), math.floor((stallInfo[0][0]-1)/2))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, K = [int(x) for x in input().split(" ")]
    answer=getDistances(K, N)
    print("Case #{}: {} {}".format(i, answer[0], answer[1]))