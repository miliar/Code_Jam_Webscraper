import sys
f = [map(int,line.split(' ')) for line in open(sys.argv[1]).read().strip().split('\n')[1:]]
out_file = open('out.txt','w')
n_case = 1
out_str = ""
for l in f:
   n_googlers, n_surprises, p = l[:3]
   sur_count = non_sur_count = 0
   t = l[3:]
   g = [(t[i]//3, t[i] - 3*int(t[i]/3.0)) for i in range(n_googlers)]
   for (n,k) in g:
      if n + ((k|(k>>1))&1) >= p: non_sur_count += 1 
      elif n>0 and n+(k>>1)+1>=p: sur_count += 1
   out_str += "Case #"+str(n_case)+": "+str(non_sur_count+min(n_surprises,sur_count))+"\n"
   n_case += 1
   
out_file.write(out_str.strip())
out_file.close()
