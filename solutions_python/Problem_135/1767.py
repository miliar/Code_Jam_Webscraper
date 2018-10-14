import sys

def solve(fin, fout):
    cases = int(fin.readline().strip())
    for index in range(cases):
        data = [];
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        data.append(fin.readline().strip().split())
        print solveCase(index+1, data)

def solveCase(index, data):
    row1 = int(data[0][0])-1
    for i in range(1,5):
        if(row1 == (i-1)):
            arow1 = data[i]

    row2 = int(data[5][0])-1
    for i in range(6,10):
        
        if(row2 == (i-6)):
            arow2 = data[i]

    #print arow1,arow2
    answer = set(arow1) & set(arow2)
    ret = ""
    if(len(answer)==1):
        ret = "Case #"+str(index)+": "+next(iter(answer))
    elif(len(answer)>1):
        ret = "Case #"+str(index)+": Bad magician!"
    else:
        ret = "Case #"+str(index)+": Volunteer cheated!"
    return ret

if __name__ == '__main__':
    solve(sys.stdin, sys.stdout)
    
