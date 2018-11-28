import sys
'''
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
'''
class Robot(object):
    def __init__(self,color):
        self.steps=[]
        self.color=color
        self.position=1
    def next(self,color,i):
        if not self.steps:
            return 0
        if self.steps[0]>self.position:
            self.position+=1
        elif self.steps[0]<self.position:
            self.position-=1
        else:
            if color==self.color:
                self.steps.pop(0)
                return 1
            else:
                return 0
        return 0
        
def calc(intMove,lstInput):
    lstTotalSteps=[(lstInput[i],lstInput[i+1]) for i in range(0,len(lstInput),2)]
    print lstTotalSteps
    oRobot=Robot('O')
    bRobot=Robot('B')
    lstRobot=[oRobot,bRobot]
    for color,button in lstTotalSteps:
        for robot in lstRobot:
            if robot.color==color:
                robot.steps.append(int(button))
    print 'Orange:',oRobot.steps
    print 'Blue:',bRobot.steps    
    i=1
    lstCurrentStep=lstTotalSteps.pop(0)
    while 1:
        pressed=0
        for robot in lstRobot:
            pressed+=robot.next(lstCurrentStep[0],i)
        if pressed:
            try:
                lstCurrentStep=lstTotalSteps.pop(0)
            except:
                break
        i+=1
    
    return i

def main():
    f=file(sys.argv[1])
    T=int(f.readline().strip())
    fOut=file('output.txt','wb')
    for i in range(1,1+T):
        s=f.readline().strip()
        lst=s.split(' ')
        output=calc(int(lst[0]),lst[1:])
        line='Case #%s: %s\r\n'%(i,output)
        print line
        fOut.write(line)
    fOut.close()
if __name__=='__main__':
    main()