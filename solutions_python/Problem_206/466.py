from os.path import expanduser
import math

problem = "A-large (1)"
path = expanduser('C:/Users/SWAPNIL/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out'
      
with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
    lines = fin.read().splitlines()
    case = 1
    a=1
    while a<len(lines):
        l=lines[a]
        d,n=map(int,l.split(' '))
        max=0
        a+=1
        for j in range(0,n):
            l=lines[a]
            ki,si=map(float,l.split(' '))
            a+=1
            if (d-ki)/si>max:
                max=(d-ki)/si
        output = 'Case #%d: %s\n' % (case,d/max)
	fout.write(output)
	case += 1

            