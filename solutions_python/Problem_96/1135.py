
infile_name=('B-large.in')
infile=open(infile_name,'r')
content=infile.readlines()
infile.close()
num=int(content[0][:-1])
outfile=open(infile_name[:-2]+'out','w')

for i in range(1,num+1):
  line_i=(content[i][:-1]).split()
  print line_i
  N=line_i[0];n=int(N)
  S=line_i[1];s=int(S)
  P=line_i[2];p=int(P)
  newline_i=0

  for j in range(n):
    if (int(line_i[3+j])/3)>=p:
      newline_i+=1
#    elif ((p-int(line_i[3+j])/3)<=2)&((p*3-int(line_i[3+j]))<=4):
    elif (0<(p*3-int(line_i[3+j]))<=2):
      newline_i+=1
    elif (2<(p*3-int(line_i[3+j]))<=4)&(s!=0)&(int(line_i[3+j])>0):
      newline_i+=1
      s-=1
#  print newline_i+'\n'
  outfile.write('Case #'+str(i)+': '+str(newline_i)+'\n')
  
outfile.close()
    

