import scipy
import sys



def main():
   if len(sys.argv) != 2:
      sys.exit(1)

   in_file =file(sys.argv[1])
   # Test cases
   N = int(in_file.readline())
   for no in range(0,N):

      line = in_file.readline().strip("\n")
      
      result = translate(line)
      

      print "Case #%d: %s" %(no+1,result)


def translate(line):
	d = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
	s =""
	for c in line:	
		if c ==" ":
			s = s + " "
		else:
			#print ord(c) -97
			s = s + d[ord(c)-97]				
	return s
			

if __name__ == "__main__":
	main()
