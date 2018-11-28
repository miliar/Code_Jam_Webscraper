import sys
from sets import Set

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

bad = 'Bad magician!'
cheated = 'Volunteer cheated!'

lines = in_file.readlines()
in_file.close()

T = int(lines[0])

index = 1
for i in range(T):
	M = int(lines[index])
	row1 = lines[index+M].split()
	index += 5
	N = int(lines[index])
	row2 = lines[index+N].split()
	index += 5
	inter = set(row1).intersection(row2)
	n = len(inter)
	if n > 1:
		out_file.write( 'Case #{0}: {1}\n'.format(i+1, bad) )
	elif n == 0:
		out_file.write( 'Case #{0}: {1}\n'.format(i+1, cheated) )
	elif n == 1:
		out_file.write( 'Case #{0}: {1}\n'.format(i+1, inter.pop()) )

out_file.close()
