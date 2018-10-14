'''
Created on 13.04.2013

@author: Alex
'''

if __name__ == '__main__':
    fileIn = open('in/B-large.in', mode='r')
    fileOut = open('out/B-large.out', mode='w')
    n = int(fileIn.readline())
    for i in range(1, n+1):
        line = fileIn.readline()
        time = 0
        done = False
        c = float(line.split()[0])
        f = float(line.split()[1])     
        x = float(line.split()[2])
        rest = x
        s = float(2)
        while done == False:
            timeIfNoMoreFarms = x / s
            timeIfOneMoreFarm = c / s + x / (s + f)
            if timeIfNoMoreFarms < timeIfOneMoreFarm:
                done = True
                time += timeIfNoMoreFarms
            else:   
                time += c / s
                s += f
        fileOut.write('Case #' + str(i) + ': ' + str(time) + '\n') 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        