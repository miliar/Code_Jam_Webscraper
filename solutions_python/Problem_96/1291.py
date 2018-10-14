import sys


def main ():
    noCases = int(sys.stdin.readline())
    for i in xrange(1,noCases+1):
        case = sys.stdin.readline()
        parts = case.split()
        googlers = int(parts[0])
        surprises = int(parts[1])
        p = int(parts[2])
        scores = []
        for j in xrange(3, len(parts)):
            scores.append(int(parts[j]))
        result = 0
        
        for score in scores:
            if(p<=1):
                if(score >= p):
                    result +=1
                continue
            
            if p + p-1 + p-1 <= score:
                result += 1
                continue
            elif p + p-2 + p-2 <= score and surprises > 0:
                surprises -=1
                result += 1
                continue
                
        print "Case #" + str(i) + ": " + str(result) 
        
    exit()

if __name__ == "__main__":
    main()