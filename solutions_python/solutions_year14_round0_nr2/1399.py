import sys

def main():
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        f = open(file)
        numOfTest = f.readline().split()[0]
        for i in range(int(numOfTest)):
            rowContent = f.readline().split()
            C = float(rowContent[0])
            F = float(rowContent[1])
            X = float(rowContent[2])
            judge(i + 1, C, F, X)
            
def judge(caseNum, C, F, X):
    a = 0
    if X < C:
        a =  X*1.0/2
    else:
        curSpeed = 2  
        a += C*1.0/curSpeed
        while(end(C, curSpeed, X, F)):
            curSpeed +=F
            a += C*1.0/(curSpeed)
        a += (X-C)*1.0/curSpeed                 
    print "Case #" + str(caseNum) + ": " + "%.7f" % a

def end(C, CurrSpeed, X, F):
    if (X-C) * 1.0/CurrSpeed <= X*1.0/(CurrSpeed + F):
        return False
    else:
        return True 
    
if __name__ == '__main__':
    main()