infile = open('A-large.in','r')
outfile = open('A-large.out','w')

T = int(infile.readline().strip('\n'))

for i in range(1,T+1):
  line = infile.readline().strip('\n')
  tokens = line.split()
  N = int(tokens[0])
  K = int(tokens[1])
  
  L = 2**N
  K = K % L
  
  if K==L-1:
    outfile.write("Case #" + str(i) + ": ON\n")
  else:
    outfile.write("Case #" + str(i) + ": OFF\n")
    
infile.close()
outfile.close()