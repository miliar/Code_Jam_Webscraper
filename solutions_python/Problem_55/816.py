import sys
import re

fin = open('input.in', 'r')
fout = open('output.out', 'w')
nos = int(fin.readline().strip())
for case in range(nos):
	lists = (fin.readline().strip()).split(" ")
	R = int(lists[0])
	k = int(lists[1])
	N = int(lists[2])
	#print R,k,N
	Ns = (fin.readline().strip()).split(" ")
	euros = 0
	for r in range(R):
		people = 0
		length = 0
		while(1):
			#print Ns
			popped = int(Ns.pop(0))
			people = people + popped
			length = length + 1
			if (Ns):
				if people > k:
					if length <= N:
						Ns.insert(0,popped)
						people = people - popped
						#print people
						euros = euros + people
						break;
				else:
					if people == k:
						Ns.append(popped)
						#print people
						euros = euros + people
						break;
					else:
						if length < N:
							Ns.append(popped)
						else:
							Ns.append(popped)
							#print people
							euros = euros + people
							break;
			else:
				if people >= k:
					Ns.insert(0,popped)
					#print people
					euros = euros + people
					break;
				else:
					euros = euros + people
					Ns.append(popped)
					break;

	#print ('Case #%(case)d: %(euros)d\n' % {'case':(case+1), 'euros':(euros)})
	fout.write('Case #%(case)d: %(euros)d\n' % {'case':(case+1), 'euros':(euros)})

fout.close()
fin.close()