
p={}
p['a']='y'
p['b']='h'
p['c']='e'
p['d']='s'
p['e']='o'
p['f']='c'
p['g']='v'
p['h']='x'
p['i']='d'
p['j']='u'
p['k']='i'
p['l']='g'
p['m']='l'
p['n']='b'
p['o']='k'
p['p']='r'
p['q']='z'
p['r']='t'
p['s']='n'
p['t']='w'
p['u']='j'
p['v']='p'
p['w']='f'
p['x']='m'
p['y']='a'
p['z']='q'
p[' ']=' '

infile_name=('A-small-attempt3.in')
infile=open(infile_name,'r')
content=infile.readlines()
infile.close()
num=int(content[0][:-1])
outfile=open(infile_name[:-2]+'out','w')

for i in range(1,num+1):
  line_i=content[i][:-1]
#  print line_i
  j=len(line_i)
  newline_i=''
  for j in range(j):
    newline_i=newline_i+p[line_i[j]]
    
#  print newline_i+'\n'
  outfile.write('Case #'+str(i)+': '+newline_i+'\n')
  
outfile.close()
    
    
  
  
  
