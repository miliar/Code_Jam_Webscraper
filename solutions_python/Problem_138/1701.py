import sys

def solve(fin, fout):
    cases = int(fin.readline().strip())
    for index in range(cases):
        ignore = (fin.readline().strip().split())
        data1 = (fin.readline().strip().split())
        data2 = (fin.readline().strip().split())
        print solveCase(index+1,data1,data2)

def solveCase(index, data1,data2):
    naomi =[]
    ken = []
    for d in data1:
        naomi.append(float(d))
    for d in data2:
        ken.append(float(d))
    

    snaomi = sorted(naomi)
    sken = sorted(ken)
    #print snaomi,sken

    naomiwin=0
    ind = 0
    for k in sken:
        while(k>snaomi[ind]):
            ind+=1
            if(ind >= len(snaomi)):
                break
        if(ind >= len(snaomi)):
            break
        naomiwin+=1
        ind+=1
        if(ind >= len(snaomi)):
            break

    kenwin=0
    ind = 0
    for k in snaomi:
        while(k>sken[ind]):
            ind+=1
            if(ind >= len(sken)):
                break
        if(ind >= len(sken)):
            break
        kenwin+=1
        ind+=1
        if(ind >= len(sken)):
            break
    ret = "Case #"+str(index)+": "+str(naomiwin)+" "+str(len(sken)-kenwin)
    return ret

if __name__ == '__main__':
    solve(sys.stdin, sys.stdout)
    
