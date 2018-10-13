import math
import pdb


def check(v1,v2,vs1,vs2):
    cc = 0
    v = 0
    for i in vs1[v1]:
        for j in vs2[v2]:
##              print i,j
              if i == j:
##                    print i,j,cc,v
                    cc+=1
                    v = i
    if cc != 1:
          if cc == 0:
                return 0
          else:
                return -1
    return v


infile = open('A-small-attempt0.in','r')
outfile = open('out.txt','w')
T = int(infile.readline())
for t in range(T):
    v1 = int(infile.readline())-1
    vs1 = []
    for i in range(4):
        vs1.append([int(a) for a in infile.readline().split(' ')])
    v2 = int(infile.readline())-1
    vs2 = []
    for i in range(4):
        vs2.append([int(a) for a in infile.readline().split(' ')])
    val = check(v1,v2,vs1,vs2)
    if val == 0:
        outfile.write('Case #'+str(t+1)+': Volunteer cheated!\n')
        print 'Case #'+str(t+1)+': Volunteer cheated!\n'
    elif val == -1:
        outfile.write('Case #'+str(t+1)+': Bad magician!\n')
        print 'Case #'+str(t+1)+': Bad magician!\n'
    else:
        outfile.write('Case #'+str(t+1)+': '+str(val)+ '\n')
        print 'Case #'+str(t+1)+': '+str(val)+ '\n'
        
infile.close()
outfile.close()
print 'Completed'
                
            
