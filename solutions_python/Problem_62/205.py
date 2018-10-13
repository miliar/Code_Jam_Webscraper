import sys

def intersect(wire1, wire2):
    t = (wire1[0] - wire2[0]) * (wire1[1] - wire2[1])
    if t > 0:
        return False
    else:
        return True
    
def calculate(wires):
    num = len(wires)
    count =  0
    for i in range(num):
        for j in range(i+1,num):
            if intersect(wires[i], wires[j]):
                count = count +1
    return count

if __name__ == "__main__":
        inFile = open(sys.argv[1])
        outFile = open(sys.argv[2],'w')
        testCaseNum = int(inFile.readline())
        for i in range(testCaseNum):
                n = int(inFile.readline())
                wires = []                
                for j in range(n):
                    params = [int(x) for x in inFile.readline().split(" ")]
                    wires.append(params)
                                                    
                outFile.write('Case #' + str(i+1) + ': ' + str(calculate(wires)) + '\n')