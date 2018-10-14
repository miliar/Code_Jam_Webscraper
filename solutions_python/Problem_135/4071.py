import sys
f = open(sys.argv[1])
o = open(sys.argv[2],'a')
T = int(f.readline())

def intersection(list1,list2):
    list = []
    for i in list1:
        for j in list2:
            if (i == j):
                list.append(i)
    return list

for i in range(1,T+1):
    firstList = []
    secondList = []
    
    first = int(f.readline())
    for j in range (0,4):
        inp = f.readline()
        List = inp.split()
        firstList.append(List)
    second = int(f.readline())
    for k in range (0,4):
        inp = f.readline()
        List = inp.split()
        secondList.append(List)
    case = intersection(firstList[first-1],secondList[second-1])
    if len(case) == 1:
        out = 'Case #'+str(i)+': '+str(case[0])
    elif len(case) > 1:
        out = 'Case #'+str(i)+': Bad magician!'
    else:
        out = 'Case #'+str(i)+': Volunteer cheated!'
    o.write(out+'\n')
o.close()