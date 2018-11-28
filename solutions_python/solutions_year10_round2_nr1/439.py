import re
import sys

def work(fp, v , n, fs):
	for i in range(0,n):
		s = fp.readline()
		if (s == "/"):
			continue;
		
		s = s[:-1]
		ss = s.split('/')
		path = ""
		#print ss
		for dic in ss:
			if (dic == ""):
				continue
			path = path + dic
			if (fs.get(path) == None):
				
				fs[path] = cnt
				v = v + 1
				#print v
				#print path
			path = path + '/'
	ret = []
	ret.append(fs)
	ret.append(v)
	return ret

if __name__=="__main__":
	fp = sys.stdin
	s = fp.readline()
	times = int (s)
	for loop in range(0,times):
		s = fp.readline()
		s = s.split(' ')
		n = int (s[0])
		m = int (s[1])
		fs = {}
		cnt = 0
		ret = work(fp, cnt, n, fs)
		fs = ret[0]
		#print fs
		
		ans = 0
		ret = work(fp, ans, m, fs)
		ans = ret[1]
		print "Case #%d: %d" %(loop+1, ans)
		
				
					
			
				
			
			
	