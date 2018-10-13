testcase_num = int(input())
fh = open('prob3.txt', 'w')
#BUild lookup table to avoid abundant calculation
lut = dict()
def lsrs(people):
    #Find Ls and Rs
    if people <= 1:
        return(0,0)
    elif people == 2:
        return(0,1)
    else:
        Ls = int(people/2)
        Rs = (int(people/2)-1) if people % 2 == 0 else int(people/2)
        return(Ls,Rs)
import collections
for testIdx in range(testcase_num):
    line = input()
    (stall, people) = map(int,(line.split()[0], line.split()[1]))
    print()
    print(str(stall) + ' ' +str(people))
    personIdx = 0
    # use a queue to record the stall sequence
    stallList = list()
    ansStallList = list()
    stallList.append(stall)
    lut[stall] = lsrs(stall)
    #print(str(stall) + ' ' + str(lut[stall]))
    #while int(len(stallList)) < people:
    while  personIdx < people:
        #print("Before")
        #print(stallList[personIdx:])
        #be = stallList[personIdx]
        stallList[personIdx:] = sorted(stallList[personIdx:], reverse=True)
        print(stallList)
        #print("After")
        #print(stallList[personIdx:])
        stallTmp = stallList[personIdx]
        #if be != stallTmp:
        #    pass
        #    print("DIFFFF")
        #    input()
        #    exit()
        personIdx += 1
        if stallTmp != 1:
            stall1 = int(stallTmp/2)
            stallList.append(stall1)
            if not lut.get(stall1):
                lut[stall1] = lsrs(stall1)
                #print(str(stall1) + ' ' + str(lut[stall1]))
            if stallTmp !=2:
                stall2 = (int(stallTmp/2)-1) if stallTmp % 2 == 0 else int(stallTmp/2)
                stallList.append(stall2)
                if not lut.get(stall2):
                    lut[stall2] = lsrs(stall2)
                    #print(str(stall2) + ' ' + str(lut[stall2]))
    stallList.sort(reverse=True)
    tgtSet = lut[stallList[people-1]]
    fh.write("Case #" + str(testIdx + 1) + ': ' + str(max(tgtSet)) + ' ' +  str(min(tgtSet)) + '\n')
    print("Case #" + str(testIdx + 1) + ': ' + str(max(tgtSet)) + ' ' +  str(min(tgtSet)))
    #print(stallList)
    print('Last : ' + str(stallList[people - 1]) + ' ' + str(lut[stallList[people - 1]]))
"""
od = collections.OrderedDict(lut.items())
for k,v in od.items(): 
    print(k, v)
    if sum(v) + 1 != k:
        print("\n\n\n\n****\n")
        exit()
"""
