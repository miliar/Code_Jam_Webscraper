
IN_FILE = 'B-small-attempt2.in.txt'
OUT_FILE = 'B-small.out.txt'


fin = open(IN_FILE)
fout = open(OUT_FILE, 'w')


T = fin.readline()

 
for t in range(int(T)):
   
   output = 0
   L = fin.readline().split()

   N = int(L[0])
   S = int(L[1])
   P = int(L[2])
   n = L[3:]


   for i in range(N):
      
      if int(n[i]) >= P:

	 x = int(n[i]) / 3
	 y = int(n[i]) % 3

	 if x >= P:
	    output += 1

	 elif y > 0 and x + 1 >= P:
	    output += 1

	 elif S > 0 and x + 1 >= P:
	    output += 1
	    S -= 1

	 elif S > 0 and y > 0 and x + 2 >= P:
	    output += 1
	    S -= 1
 
    
   fout.write('Case #' + str(t + 1) + ': ' + str(output) + '\n')


fin.close()
fout.close()

