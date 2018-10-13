#!/usr/bin/python3
import re
with open('in', 'r') as inf:
	with open('out', 'w') as outf:
		n=int(inf.readline())
		for i in range(0, n):
			countline=0
			for line in inf:
				countline=countline+1
				inar=re.split('\s+', line)
#				smax=inar[0]
				sint=inar[1]
				people=0
				print('people %s' % (people))
				out=0
				print('out %s' % (out))
				invite=0
				print('invite %s' % (invite))
				count=0
				print('count %s' % (count))
				for x in sint:
					print('x %s' % (x))
					if int(count) != int('0'):
						print('count!=0')
						while int(people) <= int(count):
							print('people %s <= count %s' % (people, count))
							people=people+1
							invite=invite+1
							print('people %s' % (out))

					people=people + int(x)
					print('people +x %s= %s' % (x, people))
					count=count + 1
					print('count +1=%s' % (count))

				out=invite
				if int(out) != 0:
					out=int(out)-1

				out=str("Case #%s: %s\n" % (countline , out))
				outf.write(out)

