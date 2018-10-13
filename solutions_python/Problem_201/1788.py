file = open("C-small-1-attempt0.in", "r")

out = open("C-small-1-attempt0.out", "w")

cases = int(file.readline())

def min(a, b):
    if a <= b:
        return a
    else:
        return b
        
def max(a, b):
    if a >= b:
        return a
    else:
        return b
        
def getSpace(array, index):
    ls = -1
    
    lpointer = index
    
    while not array[lpointer]:
        lpointer -= 1
        ls += 1
    
    lr = -1
    rpointer = index
    while not array[rpointer]:
        rpointer += 1
        lr += 1
    return ls, lr
        

for case in range(cases):

    line = file.readline().split(" ")
    
    toiletcount = int(line[0])+2
    k = int(line[1])
    

    toiletten = []
    for i in range(toiletcount):
        toiletten.append(False)
        
    toiletten[0] = True
    toiletten[len(toiletten)-1] = True
    
    lastperson = ""
    for person in range(k):
        setmin = []
        winner = (0, 0, 0)
        setmin.append((1, -1, toiletcount - 3))
        
        for i in range(len(toiletten)):
            if not toiletten[i]:
                ls, rs = getSpace(toiletten, i)
                #print(ls, rs)
                if min(ls, rs) > min( setmin[0][1], setmin[0][2]):
                    setmin = []
                    setmin.append((i, ls, rs))
                elif min(ls, rs) == min( setmin[0][1], setmin[0][2]):
                    setmin.append((i, ls, rs))
        #print(setmin)
        
        if len(setmin) > 1:
            
            setmax = []
            setmax.append(setmin[0])
            for i in range(len(setmin)):
                if max(setmin[i][1], setmin[i][2]) > max(setmax[0][1], setmax[0][2]):
                    setmax = []
                    setmax.append(setmin[i])
                elif max(setmin[i][1], setmin[i][2]) == max(setmax[0][1], setmax[0][2]):
                    setmax.append(setmin[i])
            winner = setmax[0]
        else:
            winner = setmin[0]
        toiletten[winner[0]] = True
        lastperson = winner
        
    print("Case #"+str(case+1)+": "+str(max(lastperson[1] , lastperson[2]))+" "+str(min(lastperson[1], lastperson[2])))
    out.write("Case #"+str(case+1)+": "+str(max(lastperson[1] , lastperson[2]))+" "+str(min(lastperson[1], lastperson[2]))+"\n")
    
out.close()