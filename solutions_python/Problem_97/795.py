
IN_FILE = 'C-large.in.txt'
OUT_FILE = 'C-large.out.txt'


fin = open(IN_FILE)
fout = open(OUT_FILE, 'w')


T = fin.readline()

 
for t in range(int(T)):
   
   output = 0
   keymap = { }
   A, B = fin.readline().split()
   A = int(A)
   B = int(B)

   for i in range(B - A + 1):

      keymap[str(A + i)] = {}


   for i in range(B - A + 1):

      N = str(A + i)
      
      for c in range(len(N) - 1):

	 n = N[len(N) - 1 - c:] + N[:len(N) - 1 - c]

	 if n in keymap and n != N:
	    if str(N) not in keymap[n]:
	       output += 1
	       keymap[n][str(N)] = ''
    
   fout.write('Case #' + str(t + 1) + ': ' + str(output/2) + '\n')


fin.close()
fout.close()




