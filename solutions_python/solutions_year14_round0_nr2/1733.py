import sys

def solve(fin, fout):
    cases = int(fin.readline().strip())
    for index in range(cases):
        data = (fin.readline().strip().split())
        print solveCase(index+1,data)

def recursive(c,f,x,incRate,currentTime):
    baseTime =  currentTime + x/incRate
    #print "Round",currentTime ,incRate , baseTime
    if(baseTime < currentTime + (c/incRate)+(x/(incRate+f))):
        return baseTime
    else:
        return recursive(c,f,x,incRate+f,currentTime+c/incRate)

def solveCase(index, data):
    c = float(data[0])
    f = float(data[1])
    x = float(data[2])
    ret = "Case #"+str(index)+": "+ format(recursive(c,f,x,2,0), '.7f')
    return ret

if __name__ == '__main__':
    sys.setrecursionlimit(3000)
    solve(sys.stdin, sys.stdout)
    
