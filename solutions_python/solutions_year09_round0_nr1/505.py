#
import re
f = open("A-large.in","r")
fo = open("A-large.out","w")

lines = f.readlines()
i = 0
head = lines[i].split()
L = int(head[0])
D = int(head[1])
N = int(head[2])
dic = ""
for idic in range(D):
      i = i + 1
      word = lines[i].strip()
      dic = dic + " " + word
for icase in range(N):
      i = i + 1
      w = lines[i].strip()
      w = w.replace("(","[")
      w = w.replace(")","]")
      query = re.compile(w)
      match = re.findall(query,dic)
      ans = len(match)
      print "Case #",icase+1,":",ans
      output = "Case #"+ str(icase+1)+": "+str(ans)+"\n"
      fo.write(output)
f.close()
fo.close()
