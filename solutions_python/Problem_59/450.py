'''
Created on May 22, 2010

@author: Mario
'''

def readFile(fileName):
    f = open(fileName, "r")
    
    data = f.read();
    lines = data.split('\n')
    
    x = int(lines[0])
    lines = lines[1:]
    
    result = []
    for i in range(0,x):
        numbers = lines[0].split(' ')
        lines = lines[1:]
        n = int(numbers[0])
        m = int(numbers[1])
        
        result.append((lines[0:n], lines[n:n+m]))
        lines = lines[n+m:]
    
    return result

def pathTolist(path):
    folderList = path.split('/')
    folderList = folderList[1:]
    result = []
    i = 0
    
    for folder in folderList :
        result.append(('/' + '/'.join(folderList[:i]),folder))
        i += 1
    
    return result


def addToFs(fs, path):
    n = 0
    for fromFolder,toFolder in path: 
        if toFolder not in fs[fromFolder]:
            fs[fromFolder].append(toFolder)
            if fromFolder == '/':
                key = fromFolder + toFolder
            else:
                key = fromFolder + '/' + toFolder
            if not fs.has_key(key):
                fs[key] = []
            n += 1
    return n

def processData(data):  
    f = open("output.txt", "w")
    i = 1;
    for there,new in data:
        fs = {'/' : []}
        n = 0
        for folder in there:  
            addToFs(fs, pathTolist(folder))
            
        for folder in new:  
            n += addToFs(fs, pathTolist(folder))
        
        f.write("Case #{0}: {1}\n".format(str(i), str(n)))
        i += 1
    f.close()
        
    

if __name__ == '__main__':
    data = readFile("large.in")
    processData(data)
