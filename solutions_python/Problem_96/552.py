import sys,math

score={0:(0,0),1:(1,1),2:(1,2),3:(1,2),4:(2,2),5:(2,3),6:(2,3),7:(3,3),8:(3,4),9:(3,4),10:(4,4),11:(4,5),12:(4,5),13:(5,5),14:(5,6),15:(5,6),16:(6,6),17:(6,7),18:(6,7),19:(7,7),20:(7,8),21:(7,8),22:(8,8),23:(8,9),24:(8,9),25:(9,9),26:(9,10),27:(9,10),28:(10,10),29:(10,10),30:(10,10)}

file = open(sys.argv[1])
T=file.readline()

for case, line in enumerate(file,1):
  line_list=map(int,line.split())
  N=line_list.pop(0)
  S=line_list.pop(0)
  D=line_list.pop(0)
  count=0

  for googlers in line_list:
    if score[googlers][0]>=D:
      count+=1
    elif S>0 and score[googlers][1]>=D:
      S-=1
      count+=1

  print 'Case #'+str(case)+': '+str(count)
