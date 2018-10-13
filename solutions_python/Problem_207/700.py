import numpy as np
import time

def readInputFile(fnamein):
    with open(fnamein) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content

def writeOutputFile(fnameout,outlist):        
    # Write to file
    with open(fnameout, "w") as output:
        for item in outlist:
            output.write("%s\n" % item)
             
def findMost(R=0,O=0,Y=0,G=0,B=0,V=0):
    if max(R,O,Y,G,B,V)<0:
        return 'IMPOSSIBLE'
    else:
        if R==max(R,O,Y,G,B,V):
            return 'R'
        elif O==max(R,O,Y,G,B,V):
            return 'O'
        elif Y==max(R,O,Y,G,B,V):
            return 'Y'
        elif G==max(R,O,Y,G,B,V):
            return 'G'
        elif B==max(R,O,Y,G,B,V):
            return 'B'
        elif V==max(R,O,Y,G,B,V):
            return 'V'
    
def findStallSeq(N,R,O,Y,G,B,V):
    if R>(O+Y+G+B+V) or O>(R+Y+G+B+V) or Y>(R+O+G+B+V) or G>(R+O+Y+B+V) or B>(R+O+Y+G+V) or V>(R+O+Y+G+B):
        return 'IMPOSSIBLE'
    else:
        newR,newO,newY,newG,newB,newV = R,O,Y,G,B,V
        seq = findMost(R,O,Y,G,B,V)
        if seq=='R':
            newR -= 1
        elif seq=='O':
            newO -= 1
        elif seq=='Y':
            newY -= 1
        elif seq=='G':
            newG -= 1
        elif seq=='B':
            newB -= 1
        elif seq=='V':
            newV -= 1
        for i in np.arange(1,N):        
            if seq[i-1]=='R':
                templet = findMost(0,newO,newY,newG,newB,newV)
            elif seq[i-1]=='O':
                templet = findMost(newR,0,newY,newG,newB,newV)
            elif seq[i-1]=='Y':
                templet = findMost(newR,newO,0,newG,newB,newV)
            elif seq[i-1]=='G':
                templet = findMost(newR,newO,newY,0,newB,newV)
            elif seq[i-1]=='B':
                templet = findMost(newR,newO,newY,newG,0,newV)
            elif seq[i-1]=='V':
                templet = findMost(newR,newO,newY,newG,newB,0)

            if templet=='IMPOSSIBLE':
                seq = templet
                break
            else:
                seq = seq + templet

            if templet=='R':
                newR -= 1
            elif templet=='O':
                newO -= 1
            elif templet=='Y':
                newY -= 1
            elif templet=='G':
                newG -= 1
            elif templet=='B':
                newB -= 1
            elif templet=='V':
                newV -= 1
       
        if seq=='IMPOSSIBLE':
            return seq
        elif seq[0]==seq[N-1]:
            if seq[0]!=seq[N-3]:
                seq = seq[0:(N-2)]+seq[N-1]+seq[N-2]
                return seq
            else:
                return 'IMPOSSIBLE'
        else:
            return seq

def solveB(fnamein,fnameout):
    inputlist = readInputFile(fnamein)
    outputlist = list()
    T = int(inputlist[0])
    for i in np.arange(1,T+1):
        temp_input = inputlist[i].split(' ')
        temp_N = int(temp_input[0])
        temp_R, temp_O, temp_Y = int(temp_input[1]), int(temp_input[2]), int(temp_input[3])
        temp_G, temp_B, temp_V = int(temp_input[4]), int(temp_input[5]), int(temp_input[6])
        temp_seq = findStallSeq(temp_N,temp_R,temp_O,temp_Y,temp_G,temp_B,temp_V) 
        outputlist.append('Case #'+str(i)+': '+str(temp_seq))
    writeOutputFile(fnameout,outputlist)            
    
tic = time.clock()
solveB('B-small-attempt4.in','B-small-output.txt')
toc = time.clock()
print('Runtime: '+str(toc - tic)+'sec')    