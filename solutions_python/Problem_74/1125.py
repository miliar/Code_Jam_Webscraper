'''
Created on May 7, 2011

@author: diego
'''


sample1 = "4 O 2 B 1 B 2 O 4"
sample2 = "3 O 5 O 8 B 100"
sample3 = "2 B 2 B 1"

def simulate(opath, bpath, turns):
    
    
    oPos = 1
    bPos = 1
    t = 0
    while (True):
        pressbutton=False
        if len(opath)!=0: 
            if oPos == opath[0]:
                if turns[0] == 'O':
                    '''press button'''
#                    print 'press button'
                    pressbutton=True
                    opath = opath[1:len(opath)]
                    turns = turns[1:len(turns)]
                    if len(turns) == 0:
#                        print 'finished in t:' + str(t+1)
                        break
            else:
                oPos = oPos - (oPos - opath[0]) / abs(oPos - opath[0])
        
        
        if len(bpath)!=0:
            if bPos == bpath[0]:
                if turns[0] == 'B' and not pressbutton:
                    '''press button'''
#                    print 'press button'
                    bpath = bpath[1:len(bpath)]
                    turns = turns[1:len(turns)]
                    if len(turns) == 0:
#                        print 'finished in t:' + str(t+1)
                        break
            else:
                bPos = bPos - (bPos - bpath[0]) / abs(bPos - bpath[0])
                 
        t=t+1
#        print t
#        print 'bpos:' + str(bPos) + ' oPos' + str(oPos)
    return t+1
        
        
def processPath(path):    
#    path = "O 2, B 1, B 2, O 4"
    path = path.split(",")
    path = map(lambda x: x.strip(), path)
    oPath = []
    bPath = []
    turns = []
    for step in path:
        if len(step)>0:
            if step[0] == "O":
                oPath.append(int(step[2:]))
            else: 
                bPath.append(int(step[2:]))
            
            turns.append(step[0])
        
    
    oPath=map(lambda x : int(x),oPath)
    bPath=map(lambda x : int(x),bPath)
    return simulate(oPath, bPath, turns)
        

if __name__ == '__main__':
    file=open('test.dat')
    
    lines=file.readlines()
    #ignore first line
    lines=lines[1:len(lines)]
    case=1
    for line in lines:
        while(line[0].isdigit()):
            line=line[1:]
        line=line[1:len(line)].replace('O',',O').replace('B',',B')
        print 'Case #'+str(case) +': ' + str(processPath(line))
        case=case+1
    
    
    
    
    


