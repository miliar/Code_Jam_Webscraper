#from mpmath import *
#from bigfloat import *
def find_lower_element(in_list,element):
    for i in xrange(len(in_list)):
        if in_list[i]>element:
            return i
        
def play_war(Naomi, Ken):
    points = 0
    for i in xrange(len(Naomi)):
        if Naomi[-1] > Ken[-1]:
            del Naomi[-1]
            del Ken[0]
            points+=1
        elif Naomi[-1] < Ken[-1]:
            del Ken[find_lower_element(Ken,Naomi[-1])]
            del Naomi[-1]
    return points

def play_deceitful_war(Naomi, Ken):
    points = 0
    length = len(Naomi)
    for i in range(length):
        if Naomi[i] > Ken[0]:
            del Ken[0]
            points+=1
    return points

f = open('D-large.in', 'r')
num=int(f.readline())
output=open('result','w')
case=0
base=2.0
while num!=0:
    num-=1
    case+=1
    sizeT = int(f.readline())
    Naomi = [float(x) for x in f.readline().split()]
    Ken = [float(x) for x in f.readline().split()]
    Naomi.sort()
    Ken.sort()
    #print 'Naomi - ', Naomi
    #print 'Ken - ', Ken
    pointsW = play_war(Naomi[:], Ken[:])
    pointsDW = play_deceitful_war(Naomi[:], Ken[:])
    print('Case #'+str(case)+': '+str(pointsDW)+' '+str(pointsW))
    output.write('Case #'+str(case)+': '+str(pointsDW)+' '+str(pointsW) + '\n')
output.close()
