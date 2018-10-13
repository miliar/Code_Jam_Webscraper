infile=file('A-small-attempt0.in','rb+'); outfile=file('A-small-attempt0.out','wb+')

for casen in range(1,int(infile.readline())+1):
 k=int(infile.readline()); s1=set([infile.readline() for r in range(4)][k-1].strip().split(' '))
 k=int(infile.readline()); s2=set([infile.readline() for r in range(4)][k-1].strip().split(' '))
 k=s1&s2
 if len(k)==1:   outfile.write('Case #%i: %s\r\n'%(casen,list(k)[0]))
 elif len(k)==0: outfile.write('Case #%i: %s\r\n'%(casen,'Volunteer cheated!'))
 elif len(k)>1:  outfile.write('Case #%i: %s\r\n'%(casen,'Bad magician!'))