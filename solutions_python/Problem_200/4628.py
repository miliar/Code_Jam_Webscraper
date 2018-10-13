#!/usr/bin/env python
import sys



def process(f):
    case_num = int(f.readline())
    for t in xrange(case_num):
        case_info = f.readline().strip()


        s = int(solve(case_info))
       


        print 'Case #%d: %d' % (t+1, s)
def solve(case_info):
	if tidy(case_info) == 1:
		return case_info
	else:
		last_tidy = ''
		v, p = findv(case_info)
		for i in case_info[:p]:
			last_tidy = last_tidy + i

		n = int(v)-1
		last_tidy = last_tidy + str(n)

				
		for k in case_info[p+1:]:
			last_tidy = last_tidy + '9'
		return last_tidy	
			


		

		

			

def tidy(s):
	for i in xrange(len(s)-1):

		if int(s[i]) > int(s[i+1]):
			return 0
		else:
			pass	
	return 1	

def findv(s):
	v = 0
	m = 0

	for i in xrange(len(s)-1,0,-1):
		if int(s[i]) <= int(s[i-1]):

			v = s[i-1]
			m = i-1
	
	return v, m			



def main():
    with open(sys.argv[1]) as f:
        

        process(f)

if __name__ == '__main__':
    main()