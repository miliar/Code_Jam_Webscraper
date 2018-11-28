import re
f_in = open("A-large.in","r")
f_out = open("A-large.out","w")
lines=f_in.readlines()
i=0
[L,D,N] = lines[i].split()
L=int(L)
D=int(D)
N=int(N)
dic=""
for id in range(D):
      i=i+1
      d=lines[i].strip()
      dic = dic + "," + d
for ii in range(N):
      i=i+1
      w=lines[i].strip()
      w=w.replace("(","[")
      w=w.replace(")","]")
      q=re.compile(w)
      match=re.findall(q,dic)
      ans=len(match)
      print "Case #",ii+1,":",ans
      line_o = "Case #"+ str(ii+1)+": "+str(ans)+"\n"
      f_out.write(line_o)
f_in.close()
f_out.close()
