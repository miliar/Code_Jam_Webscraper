from __future__ import print_function

def ropeIntra(wireSet, case, outFile):
    intersections = 0;
    for wire in range(0,len(wireSet)-1):
        for count in range(wire+1, len(wireSet)):
            if wireSet[wire][0] < wireSet[count][0] and wireSet[wire][1] > wireSet[count][1]:
                intersections = intersections + 1;
            elif wireSet[wire][0] > wireSet[count][0] and wireSet[wire][1] < wireSet[count][1]:
                intersections = intersections + 1;
            else:
                pass
    
    outFile.write('Case #%d: '%case)
    outFile.write('%d\n' %intersections)

print('Please enter the file name:')
fileName = raw_input()

inFile =  open(fileName, 'r')
outFile = open('RopeOutput.txt', 'w')

cases = eval(inFile.readline())
for count in range(1,cases+1):
    wires = eval(inFile.readline())
    wireSet = []
    for wire in range(0,wires):
        cur_wire = inFile.readline().split(' ')
        item = [eval(cur_wire[0]), eval(cur_wire[1])]
        wireSet.append(item)
    ropeIntra(wireSet, count, outFile)

inFile.close()
outFile.close()
