import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

def make_it_num( v ):
	for n in range( len(v) ) :
		v[n] = int( v[n] )

	
def solve(v ) :
	global pp, fs
	r = [0 for c in fs]

	for c in v :
		s = 0
		i = fs.find(c,s)
		while i >= 0  :
			if i == 0 :
				r[0] = r[0] + 1
			else :
				r[i] = r[i] + r[i-1]
			s = i+1
			i = fs.find(c,s)
		
	return r[-1]%10000
	

	
ps_time = time.time()
filename = "test"
filename = "C-small-attempt2"
filename = "C-large"

in_file = open("./"+filename+".in")
out_file = open("./"+filename+".out","w")

#getting data
fs = 'welcome to code jam'
N = int(in_file.readline().strip())

for n in range( 1, N+1 ) :	
	v = in_file.readline().strip()
		
	#solving a problem
	out =  'Case #' + str(n)
	out += ': ' 
	out += "%(#)04d" % {"#":solve(v) }
	out += '\n'
	out_file.write( out )
	print (out)

in_file.close()
out_file.close()

ps_time = time.time() - ps_time
print (ps_time)