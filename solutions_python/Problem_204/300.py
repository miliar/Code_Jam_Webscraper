import math
def rat(Rarray, NParray):
    for i in range(len(NParray)):
        NParray[i].sort()
    numKits = 0
    for i in range(len(NParray[0])):
        ingInKit = [i]
        maxServings = int(NParray[0][i]/(0.9*Rarray[0]))
        minServings = math.ceil(NParray[0][i]/(1.1*Rarray[0]))
        
        allServings = list(range(minServings, maxServings+1))
        for servings in allServings:
            percentOfTarget = NParray[0][i]/(Rarray[0]*servings)

            for j in range(1, len(NParray)): # for each ingredient
                for k in range(len(NParray[j])):
                    if k < len(NParray[j]):
                        percentOfTarget = NParray[j][k]/(Rarray[j]*servings)
                        #print('Checking ingredient #' +  str(j) + ' of size ' + str(NParray[j][k]) +  ' has percent ' + str(percentOfTarget))
                        if percentOfTarget >= .9 and percentOfTarget <= 1.1:
                            ingInKit.append(k)
                            found = True
                            break

            if len(ingInKit) == len(Rarray):
                numKits += 1
                #print('Kit has ingredients of ' + str(ingInKit))
                for  index in range(1, len(ingInKit)):
                    NParray[index].pop(ingInKit[index])
                break
        
    return numKits
	
def stringList2IntList(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    return array

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, P = input().split(" ")
    N = int(N)
    P = int(P)
    R = input().split(" ")
    R = stringList2IntList(R)
    NP = []

    for j in range(0,N):
        temp = input().split(" ")
        temp = stringList2IntList(temp)
        
        NP.append(temp)

    results =  rat(R, NP)
    print("Case #{}: {}".format(i, results))