
infile_name=('C-small-attempt0.in')
infile=open(infile_name,'r')
content=infile.readlines()
infile.close()
num=int(content[0][:-1])
outfile=open(infile_name[:-2]+'out','w')

for i in range(1,num+1):
  line_i=content[i][:-1]
  print line_i
  line_content=line_i.split()
  A=int(line_content[0])
  B=int(line_content[-1])
  line_pairs=0
  
  for j in range(A,B+1):
    n=j
    line_dig=len(str(A))

    for k in range(1,line_dig):
      m=int(str(j)[-k:]+str(j)[:line_dig-k])
      if (n>=A)&(n<m)&(m<=B):
        line_pairs+=1
        
#  print line_dig, str(line_pairs)+'\n'
  outfile.write('Case #'+str(i)+': '+str(line_pairs)+'\n')
  
outfile.close()
    
    
  
  
  
