import sys
import threading
import time

if __name__ == '__main__':
	start = int(sys.argv[2])
	end = int(sys.argv[3])
	with open(sys.argv[1]) as f:
		content = f.readlines()
		if len(content)>0:
			t = int(content[0].split('\n')[0])
					
			s = []
			l = 0
			x = 0
			
			for i in range(1, 2*t+1):
				case = content[i].split('\n')[0]
				if (i%2 == 1):
					case = case.split(' ')
					l = int(case[0])
					x = int(case[1])
				else:
					if (i/2 >= start and i/2 <= end):
						s.append((i/2-1, case*x))
					
			t = len(s)
			
			# represented in tuple (1, x) or (-1, x)
			def multiply(a, b):
				x = 1
				s = 1
				if (a[1] == '1'):
					x = b[1]
				elif (b[1] == '1'):
					x = a[1]
				elif (a[1] == 'i'):
					if (b[1] == 'i'):
						x = '1'
						s = -1
					elif (b[1] == 'j'):
						x = 'k'
					elif (b[1] == 'k'):
						x = 'j'
						s = -1
				elif (a[1] == 'j'):
					if (b[1] == 'i'):
						x = 'k'
						s = -1
					elif (b[1] == 'j'):
						x = '1'
						s = -1
					elif (b[1] == 'k'):
						x = 'i'
				elif (a[1] == 'k'):
					if (b[1] == 'i'):
						x = 'j'
					elif (b[1] == 'j'):
						x = 'i'
						s = -1
					elif (b[1] == 'k'):
						x = '1'
						s = -1
				
				return (s * a[0] * b[0], x)
			
 			q = ('1', 'i', 'j', 'k')
 			
 			mul = {}
			q = ('1', 'i', 'j', 'k')
			for a in q:
				for b in q:
					for sa in (1, -1):
						for sb in (1, -1):
							aa = (sa, a)
							bb = (sb, b)
							cc = multiply(aa,bb)
							
							if aa not in mul:
								mul[aa] = {}
								
							mul[aa][bb] = cc
			
			def multiply2(a, b):
				return mul[a][b]
 			
# 			for a in q:
# 				for b in q:
# 					print " %s *  %s = %s" % (a, b, multiply((1, a), (1, b)))
# 					print "-%s *  %s = %s" % (a, b, multiply((-1, a), (1, b)))
# 					print " %s * -%s = %s" % (a, b, multiply((1, a), (-1, b)))
# 					print "-%s * -%s = %s" % (a, b, multiply((-1, a), (-1, b)))

			div = {}
			for a in q:
				for b in q:
					for sa in (1, -1):
						for sb in (1, -1):
							aa = (sa, a)
							bb = (sb, b)
							cc = multiply(aa,bb)
							
							if cc not in div:
								div[cc] = {}
								
							div[cc][aa] = bb
							
							
			def divide(c, a):
				return div[c][a]
	
	
			def search_jk(s):
				x = (1, '1')
				y = (1, '1')
				# need to calculate k first

				for i in xrange(0, len(s)):
					y = multiply2(y, (1, s[i]))
				
				for i in xrange(len(s)-1):
					x = multiply2(x, (1, s[i]))
					y = divide(y, (1, s[i]))
					#print "  %s" % i
					#print "    %-10s %s|%s" % (x, s[0:i+1], s[i+1:len(s)] )
					if x==(1, 'j') and y==(1, 'k'):
						return True
						
				return False
		
						
			def search_i(s):
			
				x = (1, '1')
				for i in xrange(len(s)-2):
					x = multiply2(x, (1, s[i]))
					#print "%-10s %s|%s" % (x, s[0:i+1], s[i+1:len(s)] )
					if (x == (1, 'i')):
						#print "%s" % i
						#print "*"
						if search_jk(s[i+1:len(s)]):
							return True
				return False
			
			
			def search_ijk(s):
				if len(s)<3:
					return 'NO'
				
				if search_i(s):
					return 'YES'
				return 'NO'
			
			ans = {}
			semaphore = threading.BoundedSemaphore()


			def findAns(n, ss):
				global ans
				global s
				global semaphore
				
				ans[n] = search_ijk(ss)
				sys.stderr.write("Solved %s\n" % len(ans))

				semaphore.acquire()
				if len(s)>0:					
					thrd = threading.Thread(target=findAns, args = s.pop())
					semaphore.release()
					thrd.daemon = True
					thrd.start()
				else:
					semaphore.release()
			
			for i in xrange(8):
			
				semaphore.acquire()
				if (len(s) > 0):
					thrd = threading.Thread(target=findAns, args = s.pop())
					semaphore.release()
					thrd.daemon = True
					thrd.start()
				else:
					semaphore.release()
				
			
			while(True):
				if len(ans) == t:
					break
				time.sleep(0.5)
			
			for i in xrange(start-1, start+len(ans)-1):
				print "Case #%s: %s" % (i+1, ans[i])
				