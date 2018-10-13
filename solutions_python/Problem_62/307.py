'''
Created on May 23, 2010

@author: Mario
'''

def addLines(lines):
    result = []
    for line in lines:
        numbers = line.split(' ')
        result.append((int(numbers[0]),int(numbers[1])))
    return result
    
def readFile(fileName):
    f = open(fileName, "r")
    
    data = f.read();
    lines = data.split('\n')
    
    x = int(lines[0])
    lines = lines[1:]
    
    result = []
    for i in range(0,x):
        n = int(lines[0])
        lines = lines[1:]
        result.append(addLines(lines[0:n]))
        lines = lines[n:]

    return result



def processData(data):
    f = open("output.txt", "w")
    x = 1
    for case in data:
        n = 0
        for i in range(0,len(case)-1):
            for j in range(i+1, len(case)):
                if case[i][0] < case[j][0] and case[i][1] > case[j][1]:
                    n += 1
                if case[i][0] > case[j][0] and case[i][1] < case[j][1]:
                    n += 1
                    
        f.write("Case #{0}: {1}\n".format(str(x), str(n)))
        x+=1
    f.close()
        
        

if __name__ == '__main__':
    data = readFile('large.in')
    processData(data)