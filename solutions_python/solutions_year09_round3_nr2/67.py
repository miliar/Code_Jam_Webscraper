'''
Created on 2009/09/13

@author: hirobe
'''
import math

def test(fireflies):
    #print fireflies
    distance = 0.0
    avgX = float(0.0)
    avgY = float(0.0)
    avgZ = float(0.0)
    avgVX = float(0.0)
    avgVY = float(0.0)
    avgVZ = float(0.0)
    for ff in fireflies:
        avgX += float(ff[0])
        avgY += float(ff[1])
        avgZ += float(ff[2])
        avgVX += float(ff[3])
        avgVY += float(ff[4])
        avgVZ += float(ff[5])
    avgX /= len(fireflies)
    avgY /= len(fireflies)
    avgZ /= len(fireflies)
    avgVX /= len(fireflies)
    avgVY /= len(fireflies)
    avgVZ /= len(fireflies)

    if (avgVX**2+avgVY**2+avgVZ**2)==0.0:
        return (math.sqrt(avgX**2+avgY**2+avgZ**2),0.0)
    
    t = -1.0* (avgX*avgVX+avgY*avgVY+avgZ*avgVZ)/(avgVX**2+avgVY**2+avgVZ**2)
    if t<0:
        return (math.sqrt(avgX**2+avgY**2+avgZ**2),0.0)
    return (math.sqrt(((avgX+t*avgVX)**2+(avgY+t*avgVY)**2+(avgZ+t*avgVZ)**2)),t)

def read_file():
    data = []
    dataBlock = []
    isHead = True
    dataCount = 0
    blockCount = 0
    for line in open('B-large.in', 'r'):
        if isHead:
            isHead = False
        elif dataCount ==0:
            dataCount = int(line.rstrip())
            if blockCount >0:
                data.append(dataBlock)
            dataBlock = []
            blockCount +=1
        else:
            dataBlock.append(line.rstrip().split(' '))
            dataCount -=1
    data.append(dataBlock)
    return data

hoge = read_file()
#print hoge
#print math.sqrt(16)
case_index = 1
for line in read_file():
    ret= test(hoge[case_index-1])
    print "Case #%d: %.8f %.8f"%(case_index,ret[0],math.sqrt(ret[1]**2))
    case_index += 1
    