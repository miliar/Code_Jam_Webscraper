fi=file("input.txt","r")
fo=file("output.txt","w")

patt=["XXXX","XXXT","XXTX","XTXX","TXXX","OOOO","OOOT","OOTO","OTOO","TOOO"]

def won(g,w):
  for i in range(4):
    for j in range(5):
      if g[4*i:4*i+4]==patt[5*w+j]: return True
    temp=g[i]+g[4+i]+g[8+i]+g[12+i]
    for j in range(5):
      if temp==patt[5*w+j]: return True
  diag1=g[0]+g[5]+g[10]+g[15]
  diag2=g[3]+g[6]+g[9]+g[12]
  for i in range(5):
    pattern=patt[5*w+i]
    if diag1==pattern or diag2==pattern: return True
  return False
        

def not_over(g):
  for i in range(len(g)):
    if g[i]==".": return True
  return False

T=fi.readline()
res=""
for i in range(int(T)):
  s1=fi.readline()
  s2=fi.readline()
  s3=fi.readline()
  s4=fi.readline()
  s=s1.strip("\n")+s2.strip("\n")+s3.strip("\n")+s4.strip("\n")
  if won(s,0):res="Case #"+str(i+1)+": X won"
  elif won(s,1):res="Case #"+str(i+1)+": O won"
  elif not_over(s):res="Case #"+str(i+1)+": Game has not completed"
  else: res= "Case #"+str(i+1)+": Draw"
  fo.write(res+"\n")
  fi.readline()

fi.close()
fo.close()
