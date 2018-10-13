'''
Created on May 8, 2010

@author: Mario
'''



def readFile(fileName):
    f = open(fileName, "r")
    
    data = f.read();
    lines = data.split('\n')
    
    n = int(lines[0])
    lines = lines[1:n+1]
    
    result = []
    for line in lines:
        keyvalue = line.split(' ')
        result.append((int(keyvalue[0]), int(keyvalue[1])))
    return result
    

def processData(data):
    f = open("output.txt", "w")
    i = 1;
    for k,n in data :
        x = pow(2, k)
        if (n+1) % x == 0:
            f.write("Case #{0}: ON\n".format(str(i)))
        else:
            f.write("Case #{0}: OFF\n".format(str(i)))
        i += 1;
        
    f.close()
    


if __name__ == '__main__':
    data = readFile("big.in")
    processData(data)