'''
Created on 7.5.2011.

@author: Stef
'''

import sys

class Bot:
    def __init__(self,color,queue):     
        self.color = color
        self.queue = []
        for t in queue:
            if(t[0] == color):
                self.queue.append(t)
        self.position = 1;
    
    def cmd(self,now):
        if self.queue:
            next = self.queue[0]
            if next[1] == self.position:
                if now[0] == self.color:
                    self.queue.pop(0)
#                    print(self.color+" pushed button")
                    return 1
#                else:
#                    print(self.color+" stayed")
            else:
                if next[1] - self.position > 0:
                    self.position += 1
                else:
                    self.position -= 1
                
#                print(self.color+" position: "+str(self.position))
                return 0
            

def main():
    input = sys.argv[1]
    file = open(input)
    numOfTests = file.readline()
    for test in xrange(1,int(numOfTests)+1):
        line = file.readline()
        numOfButtons = int(line.split(' ')[0])
        queue = []
        lineData = map(lambda x : x.rstrip(), line.split(' ')[1:])
        for button in xrange(0,len(lineData),2):
            queue.append((lineData[button],int(lineData[button+1])))
#        print queue
        orange = Bot('O',queue)
        blue = Bot('B',queue)
        time = 0
        while numOfButtons > 0:
            now = queue[0]
            if orange.cmd(now) == 1:
                numOfButtons -= 1
                queue.pop(0)
            if blue.cmd(now) == 1:
                numOfButtons -=1
                queue.pop(0)
            time += 1
        print ("Case #" + str(test)+": "+str(time))

if __name__ == '__main__':
    main()