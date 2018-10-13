import scipy
import sys



def main():
   if len(sys.argv) != 2:
      sys.exit(1)

   in_file =file(sys.argv[1])
   # Test cases
   T = int(in_file.readline())
   for no in range(0,T):

      line = in_file.readline()
      k = map(lambda l: int(l),line.strip("\n").split())
      N = k[0]; S = k[1]; p = k[2]
      result = dance(N,S,p,k[3:])
      

      print "Case #%d: %d" %(no+1,result)


def dance(N,S,p,points):
	c = 0
	surp = 0
	
	for point in points:
		#print point % 3, point / 3
		if point == 0 and  p > 0:
			continue
		
		if point % 3 == 0 and point / 3 >= p:
			c = c + 1
			continue
 
		if point % 3 == 0 and point / 3+1 >= p:
			surp = surp + 1
			continue
		
		if point % 3 == 1 and point / 3+1 >= p:
			c = c + 1
			continue 

		if point % 3 == 2 and point / 3+1 >= p:
			c = c + 1
			continue

		if point % 3 == 2 and point / 3+2 >= p:
			surp = surp + 1
 	if surp <= S:
		c = c + surp

	else:
		c = c + S 

	return c
			

if __name__ == "__main__":
	main()
