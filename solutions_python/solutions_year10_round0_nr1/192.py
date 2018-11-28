#snapper.py
#Run on Python 2.6.5




fileName = raw_input("Enter the input filename:")
f_in = open(fileName,'r')
f_out = open('OUT'+fileName,'w')

T = int(f_in.readline())

for C in range(T):
    
  NK = f_in.readline().split(' ')
  N = int(NK[0])
  K = int(NK[1])
  
  if K > 0 and (K+1) % 2**N == 0:
    f_out.write("Case #{0}: ".format(C+1)+"ON\n")
    
  else:
    f_out.write("Case #{0}: ".format(C+1)+"OFF\n")
    
    
f_in.close()
f_out.close()